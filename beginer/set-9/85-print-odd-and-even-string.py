s = raw_input().rstrip()
evenS = oddS = ''
for i, c in enumerate(s):
	if i & 1 == 0:
		evenS += c
	else:
		oddS += c

print(evenS + " " + oddS)