def sort(values):
	for i in range(len(values)):		
		for j in range(i, len(values)):
			if (values[i] > values[j]):
				temp = values[i]
				values[i] = values[j]
				values[j] = temp

n = int(raw_input())
values = [int(x) for x in raw_input().split(" ")]
sort(values)
print(" ".join(str(x) for x in values))