#!/usr/bin/env python

FILE_PATH = "./test.txt"

def read_file(file_path=FILE_PATH):

	try:
		with open(file_path, 'r+') as input_file:
			content = [x.strip('\n') for x in input_file.readlines()]
	except BaseExeption as e:
		print(f"[x] Error: {e}")
	else:
		return content
	finally:
		input_file.close()

def parse(file_content):

	node_names = list()
	start_points, end_points = list(), list()
	nodes = dict()
	output = list()

	# Extract node names
	for f in file_content:
		if "#" in f:
			if "Node Name" in f:
				node_name = f.split(" ")[3].split(".")[0].upper()
				node_names.append(node_name)
		else:
			continue

	# Extract data start and end points
	for index, f in enumerate(file_content):
		if '"' in f and "Software Name" in file_content[index - 1]:
			start_points.append(index)
		try:
			if '"' in f and "#" in file_content[index + 1]:
				end_points.append(index + 1)
		except IndexError:
			end_points.append(index + 1)
	
	# Compile node name: data dictionary from start/endpoint slices
	for x in range(len(node_names)):
		nodes[node_names[x]] = file_content[start_points[x]:end_points[x]]

	# Create output data list {node name}, "{software name}", {version}
	for k, v in nodes.items():
		for item in v:
			software_name = item.split('"')[1]
			version = item.split('"')[3]
			item = [k, software_name, version]
			#output.append(f'{k}, "{software_name}", {version}')
			output.append(item)

	return output

if __name__ == '__main__':
	file_content = read_file()
	parsed = parse(file_content)

	for p in parsed:
		print(p)
			
			

	

		
		

	
		
