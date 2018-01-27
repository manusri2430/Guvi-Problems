values = [int(x) for x in raw_input().split(" ")]

max = values[0]
for x in values:
	if (x > max):
		max = x

print(max)

