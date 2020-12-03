#!/usr/bin/env python3

import sys

the_map = []

trees = 0

def loadMap(the_map):
	a_map = []
	# Read File
	with open(sys.argv[1]) as f:
		data = f.read().splitlines()
		for i, line in enumerate(data):		
			the_map.append([char for char in line])

def get_collision(the_map, move_y, move_x):
	searching = True
	collisions = 0
	x = 0
	y = 0
	while(searching): 
		# Tree Check
		if (the_map[x][y] == '#'): collisions += 1
		
		# Adjust
		x += move_x
		y = ((y + move_y) % width) 
		if (x >= height): searching = False

	return collisions

# Usage
if len(sys.argv) != 4:
	print("usage: part2.py input.txt")
	exit(1)

# Setup
loadMap(the_map)
move_x = int(sys.argv[3])
move_y = int(sys.argv[2])
width = len(the_map[0])
height = len(the_map)

# Find path collisions
path_one = get_collision(the_map, 1, 1)
path_two = get_collision(the_map, 3, 1)
path_three = get_collision(the_map, 5, 1)
path_four = get_collision(the_map, 7, 1)
path_five = get_collision(the_map, 1, 2)
total = path_one * path_two * path_three * path_four * path_five

# Answer
print(f"{total}");