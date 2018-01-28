def iswholeNumber(f):
	n = int(f)
	return (float(n) == f)

def isPerfectSquare(n):	
	m = n**(0.5)	
	return iswholeNumber(m)

n, m = [int(x) for x in raw_input().split(" ")]
print("Yes" if isPerfectSquare(float(n * m)) else "No")
