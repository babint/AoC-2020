#!/usr/bin/env python3

import sys
from itertools import combinations

numbers = []
found = -1

# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

# Read File + Get Numbers
with open(sys.argv[1]) as f:
	data = f.read().splitlines()

	for num in data:
		numbers.append(int(num))



# Filter and sort, ignore any number we can't use
numbers = list(filter(lambda f: int(f) < 2020, numbers))
numbers.sort()
for num1, num2, num3 in combinations(numbers, 3):
	if (found > -1): break # bail we already got an answer
	if (num1 + num2 + num3 == 2020):
		found = (num1 * num2 * num3)
		break

# Answer
print(f"{found}");