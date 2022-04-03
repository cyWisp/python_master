#!/usr/bin/env python
from ftplib import FTP

def grab_file(ftp_object):

    file_name = 'index.html'
    local_file = open(file_name, 'wb')

    ftp_object.retrbinary('RETR ' + file_name, local_file.write, 1024)

    local_file.close()

if __name__ == '__main__':

    # Define domain/server and user/pass
    creds = ('domain', 'username', 'password')

    # Establish FTP connection and log in
    ftp = FTP(creds[0])
    ftp.login(user=creds[1], passwd=creds[2])

    # Change working directory
    ftp.cwd('/public_html/')

    grab_file(ftp)
    ftp.quit()


