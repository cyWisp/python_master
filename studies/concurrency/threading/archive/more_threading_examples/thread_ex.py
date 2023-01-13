#/usr/bin/env python
import threading, os, time

def worker():


	print("this is an example of a worker")

def main():

	os.system('clear')
	time.sleep(1)
	
	threads = []

	for i in range(5):

		t = threading.Thread(target = worker)

		threads.append(t)
		t.start()

if __name__=='__main__':
	main()
