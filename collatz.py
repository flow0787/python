def collatz(number):
	if number % 2 == 0:
		number = number // 2
	else:
		number = number * 3 + 1
	return number

try:
	num = int(input("Enter a number: "))
	while num != 1:
		num = collatz(num)
		print num
except NameError:
	print("that is not a number!")