n, k = [int(x) for x in raw_input().split(" ")]
values = [int(x) for x in raw_input().split(" ")]

count = 0
for item in values:
	if item == k:
		count += 1
print(count)