#!/usr/bin/env python3

import sys
import re

seats = []

def calculate_seat(instructions):
	plane_rows = list(range(0, 128))
	plane_col =  list(range(0, 8))
	for instr in instructions:
		#print(f"row: {plane_rows}  col: {plane_col}")
		if (instr == 'F'):
			plane_rows = plane_rows[:len(plane_rows)//2]
		elif(instr == 'B'):
			plane_rows = plane_rows[(len(plane_rows)//2):]
		elif(instr == 'L'):
			plane_col = plane_col[:(len(plane_col)//2)]
		elif(instr == 'R'):
			plane_col = plane_col[(len(plane_col)//2):]
		else: 
			print(f'bad instruction: {instr}')

	seat = plane_rows[0] * 8 + plane_col[0]
	return seat


# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Read File + Get Seat
with open(sys.argv[1]) as f:
	line = f.read().splitlines()

	for instructions in line:
		seat = calculate_seat(instructions)
		seats.append(seat)


# Answer
print(f"{max(seats)}")
