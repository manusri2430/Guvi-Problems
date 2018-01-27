n = int(raw_input())
values = [int(x) for x in raw_input().split(" ")]

min = values[0]
for x in values:
	if x < min:
		min = x

print(min)