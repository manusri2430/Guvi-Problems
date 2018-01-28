import math
def isPrime(n):
	m = int(math.ceil(n**(0.5)))	
	for i in range(2, m+1):
		if n != i and n % i == 0:
			return False
	return True

n = int(raw_input())
print("Yes" if not (n < 2 or isPrime(n)) else "No")