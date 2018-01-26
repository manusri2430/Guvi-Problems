n = int(raw_input())

tempN = n
cubeSum = 0;
while tempN > 0:
	cubeSum += ((tempN %10)**3)
	tempN = tempN/10

if n == cubeSum:
	print("Yes")
else:
	print("No")