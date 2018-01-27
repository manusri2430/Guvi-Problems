n = int(raw_input())

fibonacciSeries = [1, 1];
for i in range(2, n):
	fibonacciSeries.append(fibonacciSeries[i - 2] + fibonacciSeries[i - 1])

print(" ".join(str(x) for x in fibonacciSeries))