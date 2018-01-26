import sys

m, n = [int(x) for x in raw_input().split(" ")]

oddValues = []
for i in range(m+1, n):
	if (i & 1) > 0:
		oddValues.append(str(i))

print(' '.join(oddValues))