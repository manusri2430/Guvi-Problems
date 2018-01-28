def sort(values):
	for i in range(len(values)):		
		for j in range(i, len(values)):
			if (values[i] > values[j]):
				temp = values[i]
				values[i] = values[j]
				values[j] = temp

n, k = [int(x) for x in raw_input().split(" ")]
values = [int(x) for x in raw_input().split(" ")]
sort(values)
print(values[k-1])