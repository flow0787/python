def reversal(string):
	new_string = ""
	string_len = int(len(string) - 1)
	for i in range(string_len + 1):
		new_string += string[string_len - i]
	return new_string

my_string = "bucuresti este de rahat"

print(reversal(my_string))