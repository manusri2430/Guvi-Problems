def isBinary(s):
	for c in s:
		if c != '1' and c != '0':
			return False
	return True

s = raw_input().rstrip()
print("Yes" if isBinary(s) else "No")