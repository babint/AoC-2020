#!/usr/bin/env python3

import sys
import re

passports = []
valid_passports = 0


def is_required(attr):
	return bool(fields[attr]['required'])

def has_rule(attr, rule):
	if not (attr in fields.keys()): return False
	if not (rule in fields[attr].keys()): return False
	return True

def get_rule(attr, rule):
 	return fields[attr][rule]

def check_height(attr, value):
	hgt_type = value[-2:len(value)]
	hgt_value = value[0:-2]			
	if not (hgt_type in ['cm', 'in']): 
		return False
	if (hgt_type == 'cm' and not int(hgt_value) in range(150, 194)):				
		return False
	elif (hgt_type == 'in' and not int(hgt_value) in range(59, 77)):
		return False

	# height ok 
	return True

# Validation Rules	
fields = {
	'byr': {'type':'integer', 'required':True, 'min':1920, 'max':2002},
	'iyr': {'type':'integer', 'required':True, 'min':2010, 'max':2021},
	'eyr': {'type':'integer', 'required':True, 'min':2020, 'max':2031},
	'hgt': {'type':'string', 'required':True, 'call':check_height},
	'hcl': {'type':'string', 'required':True, 'match':'^#[a-z0-9]{6}$'},
	'ecl': {'type':'integer', 'required':True, 'in_list': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']},
	'pid': {'type':'integer', 'required':True, 'match':'^[0-9]{9}$'},
	'cid': {'type':'string', 'required':False},
}

def loadPassportsold():
	with open(sys.argv[1]) as f:
		data = f.read().splitlines()
		counter = 0
		passport = {}
		for i, line in enumerate(data):		

			# new password line
			if (not line):
				passports.append(passport) 
				passport = {}
				counter += 1
				continue

			attirubtes = line.split()
			for attr in attirubtes:
				attr_data = attr.split(':')
				passport[attr_data[0]] = attr_data[1]

def loadPassports():
	with open(sys.argv[1]) as f:
		data = re.split('\n\n', f.read())
		
		for group in data:
			passport = {}
			for attrvalues in re.split(' |\n', group):
				attr, value = attrvalues.split(':')
				passport[attr] = value
			
			# Add Parsed Password
			passports.append(passport) 	
# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

loadPassports()

# Validate Passports
for passport in passports:
	valid = True

	for attr in fields:
		# Check value against rules
		try:
			value = passport.get(attr,'-1')
			if (is_required(attr) and not (attr in passport.keys())): valid = False
			if (has_rule(attr, 'min') and not (int(value) >= fields[attr]['min'])): valid = False
			if (has_rule(attr, 'max') and not (int(value) <= fields[attr]['max'])): valid = False
			if (has_rule(attr, 'match') and not (re.match(get_rule(attr, 'match'), value))): valid = False
			if (has_rule(attr, 'in_list') and not (value in get_rule(attr, 'in_list'))): valid = False
			if (has_rule(attr, 'call') and not(get_rule(attr, 'call')(attr, value))): valid = False
		except Exception as e:
			print(e)
			valid = False
	

	# Process Valid Passwords		
	if (valid):
		valid_passports +=1

	
# Answer
print(f"{valid_passports}");
