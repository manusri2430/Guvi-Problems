def sort(values):
	quickSort(values,0, len(values) - 1)

def quickSort(values, first, last):
	if first < last:
		splitPoint = partition(values, first, last)
		quickSort(values, first, splitPoint - 1)
		quickSort(values, splitPoint + 1, last)

def partition(values, first, last):
	pivotValue = values[first]

	leftMark = first + 1
	rightMark = last

	while 1:
		while leftMark <= rightMark and values[leftMark] <= pivotValue:
			leftMark = leftMark + 1

		while leftMark <= rightMark and values[rightMark] >= pivotValue:
			rightMark = rightMark - 1

		if rightMark < leftMark:
			break
		else:
			temp = values[leftMark];
			values[leftMark] = values[rightMark]
			values[rightMark] = temp

	temp = values[first]
	values[first] = values[rightMark]
	values[rightMark] = temp

	return rightMark

n = int(raw_input())
values = [int(x) for x in raw_input().split(" ")]
sort(values)
print(" ".join(str(x) for x in values))