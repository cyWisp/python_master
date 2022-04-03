#!/usr/bin/env python

def friend_or_foe(person):
	def greet_friend(t):
		return t.lower() + " :)"
	def greet_foe(t):
		return t.upper() + " >:O"

	if person == "friend":
		return greet_friend
	else:
		return greet_foe
 

if __name__ == '__main__':

	greeting = friend_or_foe("bam")
	print(greeting("hi there"))
	
