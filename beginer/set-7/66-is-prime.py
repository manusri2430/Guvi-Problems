import math
def isPrime(n):
	m = int(math.ceil(n**(0.5)))	
	for i in range(2, m):
		if n % i == 0:
			return False
	return True

n = int(raw_input())
print("Yes" if isPrime(n) else "No")