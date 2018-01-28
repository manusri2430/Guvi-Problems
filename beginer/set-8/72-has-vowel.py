def hasVowel(string):
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	for c in string:
		if c in vowels:
			return True
	return False

s = raw_input().rstrip()
print("Yes" if hasVowel(s) else "No")