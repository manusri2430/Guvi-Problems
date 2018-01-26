n, k  = [int(x) for x in raw_input().split(" ")]

values = [int(x) for x in raw_input().split(" ")]

sum = 0
for i in range(k):
	sum += values[i]

print(sum)