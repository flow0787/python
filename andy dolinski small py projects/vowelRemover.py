#! python3
# vowelRemover.py - a small script to remove voewles from a string.

message = input('Enter your message: ')
new_mesasge = ''

VOWELS = ('a', 'e', 'i', 'o', 'u')

for letter in message:
	if letter not in VOWELS:
		new_mesasge += letter

print(new_mesasge)