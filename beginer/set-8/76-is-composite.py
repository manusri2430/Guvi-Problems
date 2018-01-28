import math
def isComposite(n):
	if n == 0 or n == 1:
		return False

	m = int(math.ceil(n**(0.5)))
	for i in range(2, m + 1):
		if n % i == 0:
			return True
	return False

n = int(raw_input())
print("Yes" if isComposite(n) else "No")