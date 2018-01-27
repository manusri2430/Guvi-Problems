import sys

paragraph = sys.stdin.read().rstrip()

digitCount = 0
for x in paragraph:
	if x.isdigit():
		digitCount += 1

print(digitCount)