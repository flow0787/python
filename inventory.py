#inv = {"torch": 1, "books": 99, "arrows": 88, "maps": 5, "gold": 1324, "saddle": 1}

def inventoryItems():
	inv = {}
	while True:
		my_key = input("Enter an item: ")
		my_value = input("Enter the previous item's amount: ")
		if my_value or my_value != "":
			if my_key not in inv.keys() and my_value.isdecimal():
				inv.setdefault(my_key, []).append(my_value)
			else:
				print("The item must have a specific number as value or the item exists in the inventory already.")
				break
		else:
			break
	return inv

def displayInventory(inventory):
	print("Inventory:")
	total_items = 0
	for k, v in inventory.items():
		print(str(v) + "\t" + k)
		#total_items += v

	#print("Total intems in inventory: " + str(total_items))


inventory = inventoryItems()
displayInventory(inventory)