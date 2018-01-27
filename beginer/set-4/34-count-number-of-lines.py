import sys

paragraph = sys.stdin.read().rstrip()

terminators = 0
for x in paragraph:
	if x == '.' or x == '\n':
		terminators += 1

print(terminators + 1)