def suma(lista):
	total = 0
	for i in lista:
		total += i
	return total


def mult(lista):
	totala = 1
	for i in lista:
		totala *= i 
	return totala


lista = [1, 2, 3, 4]

print suma(lista)
print mult(lista)
