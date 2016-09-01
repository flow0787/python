#! python
# jumbledString.py - jumble a string based on random character choices

import random

string = 'this is a test string'
jumbled = ''
string = list(string)

for letter in range(0, len(string)):
	jumbled += string.pop(random.randint(0, len(string) - 1))

print(jumbled)