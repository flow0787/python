#######################
##AUTOR: BADEA FLORIN##
#######################
my_list = [4, 5, 5, 4]

#sortam lista crescator
sorted_list = sorted(my_list)

#gasim mijlocul listei
mijloc = len(sorted_list) / 2

if len(sorted_list) <= 1:
	print 1
#daca lista este de marime impara
elif len(sorted_list) % 2 != 0:
	print sorted_list[mijloc]
#daca lista este de marime para, calculam medianul din suma mijlocului si 
#celui din spate, impartit la 2, rezultat float
else:
	print (sorted_list[mijloc] + sorted_list[mijloc - 1]) / 2.0