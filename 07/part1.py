#!/usr/bin/env python3

import sys
import re

count = 0
checked = {}
matches = {}
bag_rules = {}

# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Parse File
with open(sys.argv[1]) as f:
	data = f.read().replace(' bags','').replace(' bag','').replace('.','').splitlines()
	for line in data:
		main_color, bags = line.split(' contain ')

		# Add Bag
		bag_rules[main_color] = []

		# Add Bag's Childen
		bags = bags.split(',')
		for bag in bags:	
			if (bag == 'no other'): continue # no childen		
			bag_color = bag.strip()[2:len(bag)]
			bag_num = int(bag.strip()[:1])
			bag_rules[main_color].append((bag_color, int(bag_num)))

def check_gold_bag(bag_color, depth):
	if (bag_color in checked): return checked[bag_color] # already done	
	if (bag_color == 'shiny gold'): return True # here be gold
	if (len(bag_rules[bag_color]) == 0): return False # last

	# check children
	has = False
	for rule in bag_rules[bag_color]:
		color, num = list(rule)
		if (check_gold_bag(color, (depth+1))):
			matches[color] = True
			has = True

	# Done, returned what we figured out
	checked[bag_color] = has
	if (has): matches[bag_color] = True
	return has

# Start
for bag_color in bag_rules: 
	if bag_color in checked: continue # skip
	check_gold_bag(bag_color, 0)

# Answer
print(f"{len(matches) - 1}")
