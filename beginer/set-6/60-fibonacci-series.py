def fibo(n):
	if n < 2:
		return 1
	if memo[n] != 0:
		return memo[n]
	
	memo[n] = fibo(n-2) + fibo(n-1)
	return memo[n]

n = int(raw_input())
memo = [0 for i in range(n)]
memo[0] = memo[1] = 1
fibo(n-1)
print(" ".join(str(x) for x in memo))