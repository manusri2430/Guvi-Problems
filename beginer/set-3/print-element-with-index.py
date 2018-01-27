n = int(raw_input())
values = [int(x) for x in raw_input().split(" ")]

for i, val in enumerate(values):
	print(str(val) + " " + str(i))
