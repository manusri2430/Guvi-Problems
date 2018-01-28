s = raw_input().rstrip()

newWordBegins = True
result = ''
for c in s:
	if c == ' ':
		newWordBegins = True		
	elif newWordBegins:
		newWordBegins = False
		c = chr(ord(c) - 32)
	result += c

print(result)


