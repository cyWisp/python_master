#!/usr/bin/env python
from xml.dom import minidom

if __name__ == '__main__':
	# Parse an xml file by name
	mydoc = minidom.parse('items.xml')

	items = mydoc.getElementsByTagName('item')

	# One specific item attribute
	attr_1 = items[1].attributes['name'].value
	print(f"Item #2 attribute: {attr_1}")

	# All item attributes
	print("\nAll attributes: ")
	for elem in items:
		print(elem.attributes['name'].value)

	# One specific item's data
	print("\nItem #2 data:")
	print(items[1].firstChild.data)
	print(items[1].childNodes[0].data)

	# all items data
	print("\n All item data:")
	for elem in items:
		print(elem.firstChild.data)


