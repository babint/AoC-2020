#!/usr/bin/env python3

import sys, re, string

answers = []

# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

# Read File 
with open(sys.argv[1]) as f:
	
	data = re.split('\n\n', f.read())
	for group in data:
		person_answer = []
		group_answers = list(string.ascii_letters[:26]) # 26 possible chars
		for i, char in enumerate(group):
			if (char == '\n' or (i+1) == len(group)):
				if (not char == '\n'): person_answer.append(char) # Last one in list, add before processing
				# Process this group, only keep answers they have all agreed on up to this point
				group_answers = list(set(group_answers) & set(person_answer))	
				person_answer = []
				continue
			
			# Track char to process later
			person_answer.append(char)
		
		# Count how many 'yes' answers this group all shared
		answers.append(len(group_answers))
	
		
# Answer
print(f'{sum(answers)}')
