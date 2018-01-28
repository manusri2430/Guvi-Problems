def sort(values):
	for i in range(len(values)):		
		for j in range(i, len(values)):			
			if (values[i] > values[j]):
				temp = values[i]
				values[i] = values[j]
				values[j] = temp

x = raw_input().rstrip()
xList = list(x)
sort(xList)
print("".join(xList))