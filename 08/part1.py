#!/usr/bin/env python3

import sys
import re

answer = 0
instructions = []



class GameConsole:

	def __init__(self, instructions):
		self.accumulator = 0
		self.ptr = 0
		self.tracker = [] # track what we executed
		self.error = 0
		self.instructions = instructions
		# print('--PROGRAM--')
		# for i, instruction in enumerate(instructions):
		# 	instr, val = instruction['instr'], instruction['val']
		# 	print(f'[{i}]', val, instr)
		# print('----')

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
		counter = 1
		while (self.error == 0):
			
			# Verify we haven't executed this instruction yet
			if (self.ptr in self.tracker):
				self.error = [100, f'Attempted to run instruction', (self.accumulator, self.ptr)]
				continue

			self.tracker.append(self.ptr)

			instruction = self.instructions[self.ptr]
			instr, val = instruction['instr'], instruction['val']

			#print(f'[{counter}:]', instr, val, 'ptr:', self.ptr)
			func_op = getattr(self, instr)
			func_op(instruction)

			counter += 1

		# Done Executing, return program error
		return self.error
			


# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Load Memory
with open(sys.argv[1]) as f:
	data = f.read().splitlines()
	for i, line in enumerate(data):
		instr, val = line.split(" ")
		instructions.append({'instr': instr, 'val': int(val)})


# Start
program = GameConsole(instructions)
error = program.process()


# Answer
print(f"{program.accumulator}")
