n = int(raw_input())
values = [x for x in raw_input().split(" ")]

for i, val in enumerate(values):
	print(val + " " + str(i))
