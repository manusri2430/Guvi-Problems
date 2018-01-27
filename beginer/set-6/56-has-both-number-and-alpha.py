input = raw_input()

hasAlpha = hasDigit = False
for c in input:
	if c.isalpha():
		hasAlpha = True
	if c.isdigit():
		hasDigit = True

print("Yes" if (hasAlpha and hasDigit) else "No")