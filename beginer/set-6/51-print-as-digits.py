n = int(raw_input())

digits = []
while n > 0:
	digits.append(str(n % 10))
	n = n / 10

digits = reversed(digits)

print(" ".join(digits))