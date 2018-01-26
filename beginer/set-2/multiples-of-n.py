n = int(raw_input())

result = 1;
resultList = []
for i in range(5):
	result = n * (i+1)
	resultList.append(str(result))

print ' '.join(resultList)
	