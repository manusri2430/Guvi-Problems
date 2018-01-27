input = raw_input().rstrip()

countSpaces = 0
for c in input:
	if (c == ' '):
		countSpaces += 1

print(countSpaces)