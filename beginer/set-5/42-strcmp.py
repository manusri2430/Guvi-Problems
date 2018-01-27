def myStrcmp(s1, s2):
	minLen = len(s1)
	isFirstElementGreater = False
	if len(s1) > len(s2):
		minLen = len(s2);
		isFirstElementGreater = True

	for i in range(minLen):
		if s1[i] < s2[i]:
			isFirstElementGreater = False;
			break;
		elif s1[i] > s2[i]:
			isFirstElementGreater = True;
			break;

	if isFirstElementGreater:
		return s1
	else:
		return s2

s1, s2 = [x for x in raw_input().split()]
print(myStrcmp(s1, s2))