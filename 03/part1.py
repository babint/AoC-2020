#!/usr/bin/env python3

import sys

the_map = []
searching = True
trees = 0

def loadMap(the_map):
	a_map = []
	# Read File
	with open(sys.argv[1]) as f:
		data = f.read().splitlines()
		for i, line in enumerate(data):		
			the_map.append([char for char in line])
	
# Usage
if len(sys.argv) != 4:
	print("usage: part1.py input.txt 3 1")
	exit(1)

loadMap(the_map)
move_x = int(sys.argv[3])
move_y = int(sys.argv[2])
width = len(the_map[0])
height = len(the_map)

x = 0
y = 0
while(searching): 
	# Tree Check
	if (the_map[x][y] == '#'): trees += 1
	
	# Adjust
	x += move_x
	y = ((y + move_y) % width) 
	if (x >= height): searching = False
	
# Answer
print(f"{trees}");