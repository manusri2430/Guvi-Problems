input = raw_input()

charCount = 0
for c in input:
	if (c.isalpha()):
		charCount += 1

print(charCount)