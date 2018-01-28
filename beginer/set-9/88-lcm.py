def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

x, y = [int(x) for x in raw_input().split(" ")]
if x < y:
	x, y = y, x
print((x * y) / gcd(x, y))