import sys

paragraph = sys.stdin.read().rstrip()

specialCharCount = 0
for x in paragraph:
	if not (x.isdigit() or x.isalpha() or x.isspace()):
		specialCharCount += 1

print(specialCharCount)