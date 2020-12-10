#!/usr/bin/env python3

import sys, re, copy

adaptars = []
combos = {}

# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

# Load input
with open(sys.argv[1]) as f:
	data = f.read().splitlines()
	for i, line in enumerate(data):
		adaptars.append(int(line))

def count_valid_combos(adaptars):
	if len(adaptars) in combos: return combos[len(adaptars)] # Already calculated this length
	if len(adaptars) == 1: return 1 # nothing left to count

	# Try count all valid sublists of this length
	total = 0
	prev_jolt = adaptars[0]
	for i in range(1, len(adaptars)):
		next_jolt = adaptars[i]
		if (next_jolt <= (prev_jolt+3)):
			# Check all remaining sublists from this point
			total += count_valid_combos(adaptars[i:]) 
		else: break # invalid, try next list

	# Count valid combo for this length
	combos[len(adaptars)] = total
	return total


# Start
adaptars.sort()

# Add starting power source and ending power source to list
adaptars.insert(0,0)
adaptars.append(adaptars[-1]+3)

# Run 
total_combos = count_valid_combos(adaptars)

# Answer
print(total_combos)

