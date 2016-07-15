text = raw_input("enter text")
lista = []
for i in text:
	lista.append(i)
maxim = len(lista) - 1
rev = []
for n in range(len(lista)):	
	rev.append(lista[maxim - n])
	n+=1
for x in rev:
	print x,