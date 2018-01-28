n, k = [int(x) for x in raw_input().split(" ")]
values = [int(x) for x in raw_input().split(" ")]

for item in values:
	if item & 1 != 0:
		k -= 1
		if k == 0:
			print(item)
			break
