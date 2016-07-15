text = "SUCK My duck!"
for t in text:
	if t in "AEIOUaeiou":
		text = text.replace(t, "")
print text