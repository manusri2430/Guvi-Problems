values = [int(x) for x in raw_input().split(" ")]

min = float('inf')

for item in values:
	if item < min:
		min = item

print(min)