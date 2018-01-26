import sys

n = int(sys.stdin.readline())

if n > 0:
	print("Positive")
elif n < 0:
	print("Negative")
else:
	print("Zero")
