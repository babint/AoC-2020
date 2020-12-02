#!/usr/bin/env python3

import sys
import re
 
valid_passwords = 0

# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

# Read File + Parse
with open(sys.argv[1]) as f:
	data = f.read().splitlines()

	for line in data:
		# Parse line
		pos1, pos2, letter, password = re.split('-| |: | ', line)
		pos1 = int(pos1) - 1 # offset for 0 index
		pos2 = int(pos2) - 1 # offset for 0 index
		
		# Check it only exists in one of those positions
		in_pos1 = bool(password[pos1] == letter)
		in_pos2 = bool(password[pos2] == letter)
		
		# Xor Check
		if (in_pos1 != in_pos2): 
			valid_passwords += 1
		

# Answer
print(f"{valid_passwords}");