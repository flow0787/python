#! python
#! vowelReplacer.py - replace a vowel in a stirng with a random, different one

import random

VOWELS = ('a', 'e', 'i', 'o', 'u')
message = input('Enter your message: ')
new_message = ''

for letter in message:
	if letter not in VOWELS:
		new_message += letter
	else:
		temp_vowel = random.choice(VOWELS)
		while temp_vowel == letter:
			temp_vowel = random.choice(VOWELS)
		else:
			new_message += temp_vowel

print(new_message)