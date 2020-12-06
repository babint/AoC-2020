#!/usr/bin/env python3

import sys, re

answers = []

# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Read File 
with open(sys.argv[1]) as f:	
	data = re.split('\n\n', f.read())
	for group in data:
		group_answers = {}
		group = [char for char in group]
		for yes_answers in group:
			if ((yes_answers) == '\n'): continue
			group_answers[yes_answers] = True
		
		# Finaly count of correct answers
		answers.append(len(group_answers))
		
# Answer
print(f'{sum(answers)}')
