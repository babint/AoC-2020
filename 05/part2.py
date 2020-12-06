#!/usr/bin/env python3

import sys
import re

seats = []

rows = 128
cols = 8

def caluate_id(row, col):
	return (row) * 8 + (col)

def calculate_seat(instructions, rows, cols):
	# Seat set 
	plane_rows = list(range(0, rows))
	plane_cols =  list(range(0, cols))

	# halve the seat set based on instruction
	for instr in instructions:
		if (instr == 'F'):
			plane_rows = plane_rows[:len(plane_rows)//2]
		elif(instr == 'B'):
			plane_rows = plane_rows[(len(plane_rows)//2):]
		elif(instr == 'L'):
			plane_cols = plane_cols[:(len(plane_cols)//2)]
		elif(instr == 'R'):
			plane_cols = plane_cols[(len(plane_cols)//2):]
		else: 
			print(f'bad instruction: {instr}')

	# Build Seat data from whats left 
	seat = {
		'id': caluate_id(plane_rows[0], plane_cols[0]),
		'row': plane_rows[0],
		'col': plane_cols[0]
	}

	return seat


# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

# Read File + Calculate Seat
with open(sys.argv[1]) as f:
	line = f.read().splitlines()
	for instructions in line:
		seat = calculate_seat(instructions, rows, cols)
		seats.append(int(seat['id'])) # Track seat and ids


# Find missing Seat id
missing = 0
seats.sort()
for i in range(seats[0],seats[-1]):
	if (i in seats): continue
	missing = i # found missing
	break

# Answer
print(f'{missing}')
