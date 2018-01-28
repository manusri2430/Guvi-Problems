n = int(raw_input())

digits = []
while n > 0:
	r = n % 10
	if r & 1 != 0:
		digits.append(str(r))
	n = n / 10

digits = reversed(digits)

print(" ".join(digits))