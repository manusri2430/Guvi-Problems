s = raw_input().rstrip()

digits = []
for c in s:
	if c.isdigit():
		digits.append(c)

print("".join(digits))
