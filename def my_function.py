def my_function(alist):
	alist.insert(int(len(alist) - 1), "and")
	return ", ".join(alist)

def enter_list():
	alist = []
	item = ""
	while True:
		item = input("Enter your list item: ")
		if item != "":
			alist.append(item)
		else:
			break
	return alist

spam = enter_list()

print(my_function(spam))