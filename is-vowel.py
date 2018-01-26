import sys

input = sys.stdin.readline().rstrip()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if input in vowels:
	print("Vowel")
else:
	print("Consonant")