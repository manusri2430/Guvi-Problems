n = int(raw_input())

digitsCount = 0;
while n > 0:
	n = n/10
	digitsCount += 1

print(digitsCount)