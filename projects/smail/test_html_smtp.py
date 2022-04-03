# An example implementation of mail.py
# sender and recipient are currently the same for testing purposes

#!/usr/bin/env python
from html_mail_class import Html_Message

def main():

	author = 'sender gmail address'
	rec = author #change this to preferred recipient
	acc_pass = 'password'
	sub = 'testing'
	t_message = 'this is just a test'

	h_message = '''

		<!DOCTYPE html>
		<html lang='en'>

		<html>
			<head>

				<style type='text/css'>
					p{
						color:red;
					}
				</style>

			</head>
			<body>
				<p>This is just a test</p>
			</body>
		</html>

	'''

	new_message = Html_Message(author, rec, acc_pass, sub, t_message, h_message)
	new_message.send_mail()

	print('[*] Sent')


if __name__ == '__main__':
	main()
