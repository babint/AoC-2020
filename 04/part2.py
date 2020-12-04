#!/usr/bin/env python3

import sys
import re

passports = []
valid_passports = 0

fields = {
	'byr': {'required':True},
	'iyr': {'required':True},
	'eyr': {'required':True},
	'hgt': {'required':True},
	'hcl': {'required':True},
	'ecl': {'required':True},
	'pid': {'required':True},
	'cid': {'required':False},
}

def loadPassports():
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
		
		# Add last one
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
		is_attr_valid = True
		is_required = fields[attr]['required']
		
		# If a require field is not set, skip
		if (is_required and not (attr in passport.keys())):
			valid = False
			continue

		# Validate the columns by type
		value = passport.get(attr,'')
		if (attr == 'byr' and not int(value) in range(1920, 2003)): 
			is_attr_valid = False
		elif (attr == 'iyr' and not int(value) in range(2010, 2021)): 
			is_attr_valid = False
		elif (attr == 'eyr' and not int(value) in range(2020, 2031)): 
			is_attr_valid = False
		elif (attr == 'hgt'): 
			hgt_type = value[-2:len(value)]
			hgt_value = value[0:-2]			
			if not (hgt_type in ['cm', 'in']): 
				is_attr_valid = False
			if (hgt_type == 'cm' and not int(hgt_value) in range(150, 194)):				
				is_attr_valid = False
			elif (hgt_type == 'in' and not int(hgt_value) in range(59, 77)):
				is_attr_valid = False
		elif (attr == 'hcl') and (len(value) != 7 or not re.match('^#[a-z0-9]+$', value)):
				is_attr_valid = False
		elif (attr == 'ecl' and not value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']): 
			is_attr_valid = False
		elif (attr == 'pid' and not re.match('^[0-9]{9}$', value)): 
			is_attr_valid = False

		if not (is_attr_valid):
			valid = False

	# Valid passpost		
	if (valid): 
		valid_passports +=1

	
# Answer
print(f"{valid_passports}");
