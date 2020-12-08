#!/usr/bin/env python3

import sys
import re
import copy

answer = 0
instructions = []

class GameConsole:

	def __init__(self, tape):
		self.accumulator = 0
		self.ptr = 0
		self.tracker = [] # track what we executed
		self.error = 0
		self.tape = tape
		self.length = len(tape)
		
		#self.display()
	
	def display(self, ptr=-1):
		print('--PROGRAM--')
		for i, instruction in enumerate(self.tape):
			instr, val = instruction['instr'], instruction['val']
			if (ptr == -1 or ptr == i): print(f'[{i}]', val, instr)
		print('----')

	def acc(self, instruction):
		val = instruction['val']
		#print('acc:', val, 'acc:', self.accumulator)
		self.ptr += 1
		self.accumulator += val

	def jmp(self, instruction):
		val = instruction['val']
		#print('jmp:', val, 'acc:', self.ptr)
		self.ptr += val

	def nop(self, instruction):
		#print('nop:', 0, 'acc:', self.accumulator)
		self.ptr += 1

	def process(self):
		while (self.error == 0 and (self.ptr < self.length)):
			
			# Verify we haven't executed this instruction yet
			if (self.ptr in self.tracker):
				self.error = [100, f'Attempted to run instruction: {self.ptr} twice. acc: {self.accumulator}']
			else: 
				self.tracker.append(self.ptr)

			# Figure out what intruction we are on and execute the operation
			instruction = self.tape[self.ptr]
			instr, val = instruction['instr'], instruction['val']
			func_op = getattr(self, instr)
			func_op(instruction)

		# Done Executing, return program status/error
		return self.error
			
# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

# Load Memory
with open(sys.argv[1]) as f:
	data = f.read().splitlines()
	for i, line in enumerate(data):
		instr, val = line.split(" ")
		instructions.append({'instr': instr, 'val': int(val)})


# Try and fix bad jmp/nop
for i in range(len(instructions)):	
	instr, val = instructions[i]['instr'], instructions[i]['val']	

	# Flip a targeted instruction
	if (instr == 'jmp'):	new_instr = 'nop'
	elif (instr =='nop'):	new_instr = 'jmp'
	else: 					continue # not a command we can adjust

	# start new copy of the instructions
	attempt = copy.deepcopy(instructions)
	
	# Replace old instruction
	attempt[i]['instr'] = new_instr

	# Start a new program and check answer if it exits w/o a failure
	program = GameConsole(attempt)
	if (program.process() == 0):
		answer = program.accumulator
		break #done

# Answer
print(f"{answer}")
