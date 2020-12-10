#!/usr/bin/env python3

import sys

adapters = []
combos = {}

# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

# Load input
with open(sys.argv[1]) as f:
	data = f.read().splitlines()
	for i, line in enumerate(data):
		adapters.append(int(line))

def count_valid_combos(adapters):
	if len(adapters) in combos: return combos[len(adapters)] # Already calculated this length
	if len(adapters) == 1: return 1 # nothing left to count

	# Try count all valid sublists of this length
	total = 0
	prev_jolt = adapters[0]
	for i in range(1, len(adapters)):
		next_jolt = adapters[i]
		if (next_jolt <= (prev_jolt+3)):
			# Check all remaining sublists from this point
			total += count_valid_combos(adapters[i:]) 
		else: break # invalid, try next list

	# Count valid combo for this length
	combos[len(adapters)] = total
	return total


# Start
adapters.sort()

# Add starting power source and ending power source to list
adapters.insert(0,0)
adapters.append(adapters[-1]+3)

# Run 
total_combos = count_valid_combos(adapters)

# Answer
print(total_combos)