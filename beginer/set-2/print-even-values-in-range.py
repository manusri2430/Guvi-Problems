import sys

m, n = [int(x) for x in raw_input().split(" ")]

evenValues = []
for i in range(m+1, n):
	if (i & 1) == 0:
		evenValues.append(str(i))

print(' '.join(evenValues))