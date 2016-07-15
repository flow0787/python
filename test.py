def palin(string):
	max = len(string) - 1
	mid = len(string)/2

	for s in range(mid):
		if string[s] == string[max-s]:
			return "e palindrom"
		else:
			return "nu e"
			