import math

def isPrime(n):
	m = int(math.ceil(n**(0.5)))

	for i in range(2, m):
		if(n % i == 0):
			print("No")
			return

	print("Yes")

n = int(raw_input())
isPrime(n)