#!/usr/bin/env python
if __name__ == '__main__':
	sentences = [
		"this is the first sentence",
		"this is the second sentence",
		"i like to eat apples and bananas",
		"i like to eat oranges and lemons",
		"i like to eat apples and bananas",
		"this is the first sentence",
		"this is another sentence",
		"this is where things get a little weird",
		"this is another sentence",
		"something something dark side",
		"this is another sentence",
	]

	# find duplicates
	counter = 0		
	stats = dict()

	for x in range(len(sentences)):
		test = sentences[x]
		for y in range(len(sentences)):
			if sentences[y] == test:
				counter += 1
		stats[sentences[x]] = counter
		counter = 0

	for k, v in stats.items():
		print(f"{k}: {v}")				
