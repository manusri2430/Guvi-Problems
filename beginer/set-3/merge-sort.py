def mySort(values):
	mergeSort(values, 0, len(values) - 1)

def mergeSort(values, left, right):
	if left < right:		
		mid = (left + (right-1)) / 2;
		# print("mid")
		# print(mid)
		mergeSort(values, left, mid)
		mergeSort(values, mid + 1, right)
		merge(values, left, mid, right)

def merge(values, left, mid, right):
	leftArray = []
	rightArray = []
		
	for i in range(left, mid + 1):		
		leftArray.append(values[i])

	for i in range(mid + 1, right + 1):
		rightArray.append(values[i])

	i = j = 0
	k = left
	
	while i < len(leftArray) and j < len(rightArray):
		if (leftArray[i] <= rightArray[j]):
			values[k] = leftArray[i]
			i += 1
		else:
			values[k] = rightArray[j]
			j += 1
		k += 1

	while i < len(leftArray):
		values[k] = leftArray[i]
		i += 1
		k += 1

	while j < len(rightArray):
		values[k] = rightArray[j]
		j += 1
		k += 1

n = int(raw_input())
values = [int(x) for x in raw_input().split(" ")]
mySort(values)
print(" ".join(str(x) for x in values))