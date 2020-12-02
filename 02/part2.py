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
		
		# Check it only exists in one of those positions
		if ((password[int(pos1)-1] == letter and password[int(pos2)-1] != letter)):
			valid_passwords += 1
		elif ((password[int(pos1)-1] != letter and password[int(pos2)-1] == letter)):
			valid_passwords += 1

# Answer
print(f"{valid_passwords}");