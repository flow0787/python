#######################
##AUTOR: BADEA FLORIN##
#######################
my_list = [3, 2, 2, 1]
new_list = []

#iteram in lista pentru a sterge duplicatele
for i in my_list:
	if i not in new_list:
		new_list.append(i)
print new_list