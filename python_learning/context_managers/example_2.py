#!/usr/bin/env python

class ExampleManager:
	def __init__(self, name):
		self.name = name

	def __enter__(self):
		print(f"my name is {self.name}")

	def letter(self):
		for l in self.name:
			print(l, end="")
		print()

	def __exit__(self, exc_type, exc_value, exc_traceback):
		print(f"goodbye {self.name}")



if __name__ == '__main__':
	with ExampleManager("rob") as man:
		man.letter()

	print("conext manager closed...")
