#!/usr/bin/env python3

import sys, re, copy

adaptars = []
current_volts = 0
differences = {
	0:0,
	1:0,
	2:0,
	3:0,
}

# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Load input
with open(sys.argv[1]) as f:
	data = f.read().splitlines()
	for i, line in enumerate(data):
		adaptars.append(int(line))

# Start
adaptars.sort()
for i in range(len(adaptars)):
	diff = adaptars[i] - current_volts 
	differences[diff] += 1
	current_volts = adaptars[i]

differences[3]+=1

# Answer
print(f"{differences[1] * (differences[3])}")
