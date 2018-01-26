def fillPrimesInRange(m):
	primes = [1 for i in range(m+1)]
	sqrtm = int(m**(0.5))
	primes[0] = primes[1] = 0
	for i in range(2,sqrtm):
		if primes[i] == 0:
			continue;	
		for x in xrange(i*i, m, i):
			primes[x] = 0
	
	return primes

n, m = [int(x) for x in raw_input().split(" ")]

primes = fillPrimesInRange(m)

primeValues = [];
for i in range(n+1,m):
	if primes[i]:
		primeValues.append(str(i))

print(' '.join(primeValues))



