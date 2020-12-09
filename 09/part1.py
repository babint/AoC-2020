#!/usr/bin/env python3

import sys

answer = 0
preamble_size = 25
preamble = []
numbers = []

# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Load input
with open(sys.argv[1]) as f:
	data = f.read().splitlines()
	for i, line in enumerate(data):
		if (i >= preamble_size): numbers.append(int(line))
		else: preamble.append(int(line))



def has_sum_match(num_check, nums):
	found = False
	for i, num1 in enumerate(nums):
		if (found == True): break
		for j, num2 in enumerate(nums):			
			if (i == j): break # don't attempt to sum itself			
			if (found == True): break # don't attempt if we are done 
			if ((num1 + num2) == num_check): found = True # Match Check
	return found

# Start
numbers_size = len(numbers)
for i in range(0,numbers_size):
	# Check Number for sum match
	num = numbers.pop(0)
	if not (has_sum_match(num, preamble)):
		answer = num
		break

	# Adjust Preamble
	preamble.pop(0)
	preamble.append(num)

# Answer
print(f"{answer}")
