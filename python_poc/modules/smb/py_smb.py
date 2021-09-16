
# https://gist.github.com/joselitosn/e74dbc2812c6479d3678
from smb.SMBConnection import SMBConnection

userID = 'user'
password = 'password'
client_machine_name = 'localpcname'

server_name = 'servername'
server_ip = '0.0.0.0'

domain_name = 'domainname'

conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True,
                     is_direct_tcp=True)

conn.connect(server_ip, 445)

shares = conn.listShares()

for share in shares:
    if not share.isSpecial and share.name not in ['NETLOGON', 'SYSVOL']:
        sharedfiles = conn.listPath(share.name, '/')
        for sharedfile in sharedfiles:
            print(sharedfile.filename)

conn.close()

# with open('pysmb.py', 'rb') as file:
#     conn.storeFile('remotefolder', 'pysmb.py', file)
