#!/usr/bin/env python
import time, os, sys

def getQuestions(chapter):

	try:
		with open(chapter, 'r') as chapterQuiz:
			allQestions = chapterQuiz.realines()
	except:
		print("Could not open file...")
	finally:
		chapterQuiz.close()

	
		


def main():

	

if __name__=='__main__':
	main()
