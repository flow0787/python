
allGuests = {"Alice": {"apples": 5, "pretzels": 12},
			 "Bob": {"ham sandwiches": 3, "apples": 2},
			 "Carol": {"cups": 3, "apple pies": 1}}

def totalBrought(guests, items):
	numBrought = 0
	for k, v in guests.items():
		numBrought = numBrought + v.get(items, 0)
	return numBrought

print("Number of things being brought:")
print(" - apples	" +str(totalBrought(allGuests, "apples")))
print(" - cups 		" +str(totalBrought(allGuests, "cups")))