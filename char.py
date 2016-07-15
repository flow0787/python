def char(string):
	if len(string) == 1:		
		for i in string:
			if i not in "aeiouAEIOU":
				return False
			else:
				return True
	else:
		return "string is larger than 1 character"
string = "a"

print char(string)