#!/usr/bin/env python
from ftplib import FTP

if __name__ == '__main__':

    # Domain name or server ip
    ftp = FTP('url')
    ftp.login(user='user', passwd='password')

    # Change working directory to "public_html and show contents"
    ftp.cwd('/public_html/')
    ftp.dir()
