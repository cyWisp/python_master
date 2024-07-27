#!/usr/bin/python3
import os
import profile
import sys
import boto3
import requests
import configparser
import base64
import defusedxml.ElementTree as DT
import re
from bs4 import BeautifulSoup
from os.path import expanduser
from urllib.parse import urlparse, urlunparse
from botocore.exceptions import BotoCoreError
from botocore.exceptions import ClientError
from onepassword import OnePassword
import datetime
import json
import argparse
from time import gmtime
from json import JSONEncoder
import logging

logger = logging.getLogger(__name__)
pid = os.getpid()
class DateTimeEncoder(JSONEncoder):
    #Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

def parse_args():
    parser = argparse.ArgumentParser()
    # Default AWS region that this script will connect to for all API calls
    parser.add_argument('--r', dest='region', help='Region Name', default='us-east-1', type=str)
    parser.add_argument('--arn', dest='arn', help='Role ARN', default='', type=str)
    parser.add_argument('--c', dest='cache_file', help='Cache File', default='/.aws/token_cache.json', type=str)
    return parser.parse_args()


def cred_output(creds):
    creds['Version'] = 1
    sys.stdout.write(json.dumps(creds, default=str))


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

home = expanduser("~")
log_file = home + "/.aws/adfs.log"
FORMAT = f"%(asctime)s {pid} %(message)s"
logging.basicConfig(filename=log_file, level=logging.INFO, format=FORMAT)
args = parse_args()


# Variables
region = args.region
cache_file = home + args.cache_file
role_arn = args.arn

logger.info(f"started, region: {region}, cache: {cache_file}, role: {role_arn}")



try:
    logger.info("attempting to load cache")
    with open(cache_file, 'r') as cache:
        credentials = json.load(cache)
        now = datetime.datetime.now(datetime.UTC)
        if datetime.datetime.fromisoformat(credentials['Expiration']) >= now:
            cred_output(credentials)
            logger.info("cache used successfully")
            exit(0)

except Exception as e:
    logger.info(f"cache not usable {e} - fetching creds")

# SSL certificate verification
sslverification = True
# idp url for authentication process.
identity_url = 'https://sts.qualnet.org/adfs/ls/IdpInitiatedSignOn.aspx?loginToRp=urn:amazon:webservices'
op = OnePassword('app', 'my')
uuid = op.get_uuid('Servicenowservices')
info = op.get_item(uuid)['fields']

usernameField = next(f for f in info if f['id'] == 'username')
username = usernameField['value']

pwField = next(f for f in info if f['id'] == 'password')
password = pwField['value']

mfaField = next(f for f in info if f['type'] == 'OTP')
mfacode = mfaField['totp']


#Solution
try:

    # Initiate session handler
    with requests.Session() as session:

        # Programmatically get the SAML assertion
        formresponse = session.get(identity_url, verify=sslverification)

        # Capture the idpauthformsubmiturl
        idpauthformsubmiturl = formresponse.url

        # Parse the response and extract all the necessary values
        formsoup = BeautifulSoup(formresponse.text,"html.parser")
        payload = {}
        for inputtag in formsoup.find_all(re.compile('(INPUT|input)')):
            name = inputtag.get('name','')
            value = inputtag.get('value','')
            if "user" in name.lower():
                #Make an educated guess that this is the right field for the username
                payload[name] = username
            elif "email" in name.lower():
                #Some IdPs also label the username field as 'email'
                payload[name] = username
            elif "pass" in name.lower():
                #Make an educated guess that this is the right field for the password
                payload[name] = password
            else:
                #Simply populate the parameter with the existing value (picks up hidden fields in the login form)
                payload[name] = value

        for inputtag in formsoup.find_all(re.compile('(FORM|form)')):
            action = inputtag.get('action')
            loginid = inputtag.get('id')
            if (action and loginid == "loginForm"):
                parsedurl = urlparse(identity_url)
                idpauthformsubmiturl = parsedurl.scheme + "://" + parsedurl.netloc + action

        # Performs the submission of the IdP login form with the above post data
        initialresponse = session.post(idpauthformsubmiturl, data=payload, verify=sslverification)

        # Overwrite and delete the credential variables
        del username
        del password

        if "Incorrect user ID or password. Type the correct user ID and password, and try again." in initialresponse.text:
            raise Exception("Incorrect user ID or password. Type the correct user ID and password, and try again.")

        # Decode the response and extract the SAML assertion
        soup = BeautifulSoup(initialresponse.text,"html.parser")
        assertion = ''
        samlresponseencoded=''
        vipauthformsubmiturl=''

        # Look for the SAMLResponse attribute of the input tag
        for inputtag in soup.find_all('input'):
            if(inputtag.get('name') == 'SAMLResponse'):
                samlresponseencoded = inputtag.get('value')

        # If SAMLResponse not found then Look for the VIP AuthMethod
        if not samlresponseencoded:
            if(soup.find('input',id='authMethod').get('value') == 'VIPAuthenticationProviderWindowsAccountName'):
                if (soup.find('input',id='vippassword')):
                    #print("VIP or MFA Token:", end=' ')
                    #mfacode = input()
                    payload['Context'] = soup.find('input',id='context').get('value')
                    payload['security_code'] = mfacode

                    for inputtag in soup.find_all(re.compile('(FORM|form)')):
                        loginid = inputtag.get('id')
                        if (loginid == "loginForm"):
                            vipauthformsubmiturl = soup.find('form',id='options').get('action')
                    # Performs the submission of the IdP login form with the above post data
                    vipresponse = session.post(vipauthformsubmiturl, data=payload, verify=sslverification)

            if vipresponse:
                if "Authentication failed due to invalid security code or server error. If there are many unsuccessful login attempts, your account will be locked." in vipresponse.text:
                    logger.error('Authentication failed due to invalid security code or server error. If there are many unsuccessful login attempts, your account will be locked.')
                    sys.exit(0)
                # Decode the response and extract the SAML assertion
                stssoup = BeautifulSoup(vipresponse.text,"html.parser")
                # Look for the SAMLResponse attribute of the input tag
                for inputtag in stssoup.find_all('input'):
                    if(inputtag.get('name') == 'SAMLResponse'):
                        samlresponseencoded = inputtag.get('value')

        assertion = samlresponseencoded

        # Better error handling is required for production use.
        if (assertion == ''):
            raise Exception("Invalid assertions in ADFS response")

        # Parse the returned assertion and extract the authorized roles
        awsroles = []
        root = DT.fromstring(base64.b64decode(assertion))

        for saml2attribute in root.iter('{urn:oasis:names:tc:SAML:2.0:assertion}Attribute'):
            if (saml2attribute.get('Name') == 'https://aws.amazon.com/SAML/Attributes/Role'):
                for saml2attributevalue in saml2attribute.iter('{urn:oasis:names:tc:SAML:2.0:assertion}AttributeValue'):
                    awsroles.append(saml2attributevalue.text)

        for awsrole in awsroles:
            chunks = awsrole.split(',')
            if'saml-provider' in chunks[0]:
                newawsrole = chunks[1] + ',' + chunks[0]
                index = awsroles.index(awsrole)
                awsroles.insert(index, newawsrole)
                awsroles.remove(awsrole)

        # If More than one role, ask the user which one they want otherwise just proceed

        role = next(f for f in awsroles if f.split(',')[0] == role_arn)
        role_arn = role.split(',')[0]
        principal_arn = role.split(',')[1]


    # Use the assertion to get an AWS STS token using Assume Role with SAML
    try:
        conn = boto3.client('sts',region)
        token = conn.assume_role_with_saml(RoleArn=role_arn, PrincipalArn=principal_arn, SAMLAssertion=assertion)
    except Exception as e:
        logger.error("Error: {}".format(e))
        raise Exception("Failure calling AWS STS service.  Likely issues: a) Outgoing internet connectivity or b) Problem with ADFS trust, claims, or role.")

    # Output credentials so that aws cli can consume them
    credentials = token['Credentials']

    creds = json.dumps(token['Credentials'], cls=DateTimeEncoder)
    with open(cache_file, 'w+') as cache:
        cache.write(creds)

    cred_output(credentials)
except (KeyboardInterrupt, SystemExit):
    raise
except KeyError as e:
    logger.error("KeyError: {}".format(e))
except (BotoCoreError, ClientError) as e:
    logger.error("{}".format(e))
except Exception as e:
    logger.error("{}".format(e))

logger.info('done')