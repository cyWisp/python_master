#!/usr/bin/env python

if __name__ == '__main__':

	try:
		raise Exception
	except BaseException:
		print("a", end='')
	except Exception:
		print("b", end='')
	except:
		print("c", end='')
	finally:
		print("c")
