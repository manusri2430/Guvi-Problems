n = int(raw_input())
values = [int(x) for x in raw_input().split(" ")]

sum = 0
for x in values:
	sum += x

print(sum / n)