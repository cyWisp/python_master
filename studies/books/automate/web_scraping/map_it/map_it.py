#!/usr/bin/env python
import webbrowser, sys, pyperclip

def main():

	if len(sys.argv) > 1:
		address = ' '.join(sys.argv[1:])
	else:
		address = pyperclip.paste()
		
	webbrowser.open('https://www.google.com/maps/place/{}'.format(address))

if __name__ == '__main__':
	main()
