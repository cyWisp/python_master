#!/usr/bin/env python
from ftplib import FTP

if __name__ == '__main__':

    session = FTP('domain', 'username', 'password')
    upload_file = open('test.txt', 'rb')

    session.storbinary('STOR test.txt', upload_file)
    upload_file.close()
    session.quit()
