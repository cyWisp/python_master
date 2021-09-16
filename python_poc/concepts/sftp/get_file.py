#!/usr/bin/env python
import pysftp

if __name__ == '__main__':

	user_name, password = 'username', 'password'
	host = "hostname"

	try:
		with pysftp.Connection(
			host, 
			username=user_name, 
			password=password
		) as sftp:
			with sftp.cd("/home/wisp/sftp_test"):
				sftp.get("./get_file.txt")
	except Exception as e: print(f"[x] error: {e}")
