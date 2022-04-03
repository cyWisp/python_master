#!/usr/bin/env python
import time, os, sys

def main():

	roles = {'top':'garen','mid':'katarina','jungle':'nidalee','adc':'ezreal','support':'leona'}

	print("Our team structure is as follows:\n\nWe will have {} in the top lane, {} in the bottom lane, {} jungling, {} as our adc and {} picking up support".format(str(roles['top']), str(roles['mid']), str(roles['jungle']), str(roles['adc']), str(roles['support'])))

	


if __name__=='__main__':
	main()
