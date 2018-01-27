n = int(raw_input())
values = [int(x) for x in raw_input().split(" ")]

min = float("inf")
max = 0

for x in values:
	if x > max:
		max = x
	if x < min:
		min = x

print(str(min) + " " + str(max))