def isNumber(str):
	if str[0] != '-' and not str[0].isdigit():
		return False
	if str[0] == '-' and len(str) == 1:
		return False
	for i in range(1, len(str)):		
		if not str[i].isdigit():
			return False
	return True

input = raw_input()

if (isNumber(input)):
	print("Yes")
else:
	print("No")
