def reverseNumber(number):
	reversedNumber = 0
	while number > 0:
		remainder = number % 10
		reversedNumber = (reversedNumber * 10) + remainder;
		number = number / 10;
	return reversedNumber

number = int(raw_input())
if number == reverseNumber(number):
	print("Yes")
else:
	print("No")

