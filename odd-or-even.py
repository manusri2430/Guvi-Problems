import sys

n = int(sys.stdin.readline())

if n & 1 == 0:
	print("Even")
else:
	print("Odd")