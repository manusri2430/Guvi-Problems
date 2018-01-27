def nextPowerOf2(n):
	count = 0

	if n == 0:
		return 1

	if not (n & (n-1)):
		return n << 1

	while n != 0:
		n = n >> 1
		count += 1

	return 1 << count

n = int(raw_input())
print(nextPowerOf2(n))