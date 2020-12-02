#!/usr/bin/env python3

import sys
import re
 
valid_passwords = 0

# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Read File + Parse
with open(sys.argv[1]) as f:
	data = f.read().splitlines()

	for line in data:
		# Parse line
		min_num, max_num, letter, password = re.split('-| |: | ', line)
		occurs = password.count(letter)
		
		# Check Policy
		if (occurs >= int(min_num) and occurs <= int(max_num)):
			valid_passwords += 1 

# Answer
print(f"{valid_passwords}");