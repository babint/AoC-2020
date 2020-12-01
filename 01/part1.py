#!/usr/bin/env python3

import sys

numbers = []
found = -1
# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Read File + Get Numbers
with open(sys.argv[1]) as f:
	data = f.read().splitlines()

	for num in data:
		numbers.append(int(num))

# Start 
for i, num1 in enumerate(numbers):
	if (found > -1): break
	for j, num2 in enumerate(numbers):
		#print(f'i: {i} num: {num1} j: {j} num2: {num2}')

		# don't attempt to sum itself
		if (i == j): break 

		# don't attempt if we are done 
		if (found > -1): break

		# Match?
		if ((num1 + num2) == 2020): 
			found = (num1 * num2)

# Answer
print(f"{found}");