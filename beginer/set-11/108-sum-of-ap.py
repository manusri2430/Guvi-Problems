a, b, c = [int(x) for x in raw_input().split(" ")]

sum = 0
for i in range(c):
	sum += a + (i * b)

print(sum)