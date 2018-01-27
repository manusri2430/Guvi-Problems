n, a, d = [int(x) for x in raw_input().split(" ")]

sum = 0
for i in range(n):
	sum += a + (i * d)

print(sum)