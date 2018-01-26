def getAmstrongValue(n):
	cubeSum = 0;
	while n > 0:
		cubeSum += ((n %10)**3)
		n = n/10

	return cubeSum

n, m = [int(x) for x in raw_input().split(" ")]

amstrongValues = []
for i in range(n+1, m):
	if i == getAmstrongValue(i):
		amstrongValues.append(str(i))

print ' '.join(amstrongValues)