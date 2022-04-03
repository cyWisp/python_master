#!/usr/bin/env python
from sys import argv, exit
import os

TEMPLATE = """#!/usr/bin/env python
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

TITLE = "Template"
RES = (800, 600)

def quit_game():
    pygame.quit()
    quit()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(RES)
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        
        

        pygame.display.flip()
        clock.tick(60)
    quit_game()
"""
def usage():
	print(f"[!] Usage: {argv[0]} [<script name>]")
	exit()

def get_params():
	if len(argv) <= 2:
		if len(argv) == 1: name = "template.py"
		else: name = f"{argv[1]}.py"
		return name
	else: usage()
	
def write_template(name):
	o_path = os.path.join("./", name)
	try:
		with open(o_path, 'w') as out_file:
			for line in TEMPLATE:
				out_file.write(line)
	except Exception as e: print(f"[x] Error: {e}")
	else: print(f"[+] {o_path} written successfully!")
	
if __name__ == '__main__':
	name = get_params()
	write_template(name)

