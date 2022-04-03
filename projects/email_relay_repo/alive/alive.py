#!/usr/bin/env python
import os, time, argparse
from mail import Html_Message
from datetime import datetime

def get_station_ips():

    file_path = './ip_list'
    file_path = os.path.abspath(file_path)
    
    stations = []
    kiosk_data = []

    for root, subs, files in os.walk(file_path):
        for f in files:
            stations.append(f)

    for station in stations:
        temp_path = os.path.join(file_path, station)
        try:
            with open(temp_path, 'r') as station_data:
                for line in station_data:
                   entry = {str(line[:7]):str(line[8:].rstrip('\n'))}
                   kiosk_data.append(entry) 
        except:
            print('[x] Could not open file for reading...')
        finally:
            station_data.close()

    #for record in kiosk_data:
    #   for key, val in record.items():
    #        print('name: {0} | ip: {1}'.format(str(key), str(val)))
    
    return kiosk_data
    
def ping_kiosks():

    kiosks = get_station_ips()
    name = []
    ip = []
    
    for k in kiosks:
        for key, val in k.items():
            command = "ping -n 1 {} > ./temp.txt".format(val)
            os.system(command)

            with open('./temp.txt', 'r') as temp_file:
                for line in temp_file:
                    if line == '\n':
                        pass
                    else:
                        if not "Received" in line:
                            pass
                        else:
                            if "Received = 1" in line:
                                pass
                                #print('Name: {0}, IP: {1}, Status: Online'.format(key, val))
                                #results.append("Host is UP")
                            elif "Received = 0":
                                #offline_kiosk = 'Kiosk: {0}, IP: {1}, Status: Offline'.format(key, val)
                                #offline.append(offline_kiosk)
                                name.append(key)
                                ip.append(val)
                                #results.append("Host is Down")
            temp_file.close()
            os.remove('./temp.txt')
    
    for index, k in enumerate(name):
        print(k + ": " + ip[index])

    return name, ip

def create_notification(kiosk_name, kiosk_ip):

    table_data = []

    html_head = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title></title>
        <style type='text/css'>
            body {
                margin-left: 5px;
                margin-top: 5px;
                margin-right: 0px;
                margin-bottom: 10px;
            }
            table{
                border: thin solid #000000;
            }
            td{
                font-family: Tahoma;
                font-size: 11px;
                border-top: 1px solid #999999;
                border-right: 1px solid #999999;
                border-bottom: 1px solid #999999;
                border-left: 1px solid #999999;
                padding-top: 0px;
                padding-right: 0px;
                padding-bottom: 0px;
                padding-left: 0px;
            }
        </style>
    </head> 
    """

    for index, k in enumerate(kiosk_name):
        data_item = """
        <tr>
            <td bgcolor= 'GainsBoro' align=center><B>{0}</B></td>
            <td bgcolor= 'GainsBoro' align=center><B>{1}</B></td>
            <td bgcolor= 'red' align=center><B>OFFLINE</B></td>
        </tr>""".format(k, kiosk_ip[index])

        table_data.append(data_item)

    html_body_1 = """
    <body>
        <table width='100%'>
            <tr bgcolor='0C0C0B'>
                <td colspan='7' height='25' align='center'>
                <font face='tahoma' color='#FBFB06' size='4'><strong>ITOC Hourly Kiosk Report</strong></font>
                </td>
            </tr>
        </table>
        <table width='100%'>
            <thead>
                <tr bgcolor='0C0C0B'>
                    <td width='15%' align='center'><font face='tahoma' color='#FBFCFC'><B>Kiosk ID</B></font></td>
                    <td width='30%' align='center'><font face='tahoma' color='#FBFCFC'><B>Kiosk IP</B></font></td>
                    <td width='15%' align='center'><font face='tahoma' color='#FBFCFC'><B>Status</B></font></td>
                </tr>
            </thead>
            <tbody>
    """
    #===================================
    with open('temp_2.txt', 'w') as temp:
        for td in table_data:
            temp.write(td)
    temp.close()

    html_body_2 = ""

    with open('temp_2.txt', 'r') as temp:
        list_object = temp.readlines()
        html_body_2 = ''.join(list_object)
    temp.close()
    os.remove('temp_2.txt')
    #===================================

    html_body_3 = """     
            </tbody>
        </table>

    </body>
    </html>
    """
    notification = html_head + html_body_1 + html_body_2 + html_body_3

    #with open('output.txt', 'w') as output:
    #    output.write(notification)
    #output.close()

    return notification

def send_notification(formatted_data):
    
    author = 'example@example.com'
    rec = 'example@example.com'
    sub = 'Your Report Name Here {}'.format(datetime.now())
    msg = 'Your Report Results: '
        
    email_notification = Html_Message(author, rec, sub, msg, formatted_data)
    email_notification.send_mail()

    print('[*] Email Sent!')

if __name__ == '__main__':
    kiosk, address = ping_kiosks()
    notification_message = create_notification(kiosk, address)
    send_notification(notification_message)

    
  
