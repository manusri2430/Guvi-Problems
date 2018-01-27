input = raw_input().rstrip()

countSpaces = 0
for c in input:
	if (c == ' '):
		countSpaces += 1

# number of words = number of spaces + 1
print(countSpaces + 1)