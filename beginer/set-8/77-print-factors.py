n = int(raw_input())

factors = []
for i in range(1, n+1):
	if n % i == 0:
		factors.append(str(i))

print(" ".join(factors))