#!/usr/bin/env python3

import sys

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
	print("usage: part1.py input.txt")
	exit(1)

loadPassports()

# Validate Passports
for passport in passports:
	valid = True
	for attr in fields:
		is_required = fields[attr]['required']
		# If a require field is not set, skip
		if (is_required and not (attr in passport.keys())):
			valid = False
			continue
	if (valid): valid_passports +=1

	
# Answer
print(f"{valid_passports}");


