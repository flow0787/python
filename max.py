def maxim(x, y):
	if x > y:
		return "%s is maxim" %x
	elif x == y:
		return "x is equal to y"
	else:
		return "%s is maxim" %y

def max_of_three(x, y, z):
	if x > y and x > z:
		return "%s is max" %x
	elif y > x  and y > z:
		return "%s is max" %y
	elif z > x and z > y:
		return "%s is max" %z

print max_of_three(55, 21, 230)