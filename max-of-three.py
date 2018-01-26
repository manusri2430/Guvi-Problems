def maxOfTwo(x, y):
	if x > y:
		return x
	else:
		return y;

def maxOfThree(x, y, z):
	return maxOfTwo(x, maxOfTwo(y, z))

x, y, z = [int(x) for x in raw_input().split(" ")]
print(maxOfThree(x,y,z))