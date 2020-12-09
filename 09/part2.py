#!/usr/bin/env python3

import sys

preamble = []
numbers = []
all_numbers = []

# Usage
if len(sys.argv) != 3:
	print("usage: part2.py input.txt #")
	exit(1)

preamble_size = int(sys.argv[2])
if not (preamble_size > 0):
	print("usage: part2.py input.txt preamble_size")
	exit(1)

# Load input
with open(sys.argv[1]) as f:
	data = f.read().splitlines()
	for i, line in enumerate(data):
		if (i >= preamble_size): numbers.append(int(line))	# build preamble
		else: preamble.append(int(line))					# build rest of numbers
		all_numbers.append(int(line))


def has_sum_match(num_check, nums):
	found = False
	for i, num1 in enumerate(nums):
		if (found == True): break
		for j, num2 in enumerate(nums):			
			if (i == j): break # don't attempt to sum itself			
			if (found == True): break # don't attempt if we are done 
			if ((num1 + num2) == num_check): found = True # Match Check
	return found

def find_invalid_numbers(preamble, numbers):
	invalid_number = -1
	numbers_size = len(numbers)
	for i in range(0,numbers_size):
		num = numbers.pop(0) # grab number sum match
		if not (has_sum_match(num, preamble)):
			invalid_number = num
			break

		# Move number to preamble, keeping same size
		preamble.pop(0)
		preamble.append(num)

	return invalid_number

def subset_sum(data, sum_target):
	data_size = len(data) 
	for i in range(data_size):
		# Grab first item for sum and move to next item
		curr_sum = data[i] 
		ptr = (i + 1)

		# Keep adding until we are larger than the number we want 
		while ptr <= data_size:
			# Exact Sum, done
			if curr_sum == sum_target: return (i, ptr)
			
			# Too much, bail
			if curr_sum > sum_target or ptr == data_size: 	break
			
			# Moving along
			curr_sum = curr_sum + data[ptr] 
			ptr += 1
 	
 	# Nothing
	return (0,0)

# Start
invalid_number = find_invalid_numbers(preamble.copy(), numbers.copy())
start, stop = subset_sum(all_numbers, invalid_number)
sublist = all_numbers[start:stop]
sublist.sort()

# Answer
print(f"{sublist[0] + sublist[-1]}")
