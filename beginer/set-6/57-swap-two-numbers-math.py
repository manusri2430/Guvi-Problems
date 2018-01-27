n, m = [int(x) for x in raw_input().split(" ")] # n = 10, m = 5
n = n + m # n = 15, m = 5
m = n - m # n = 15, m = 10
n = n - m # n = 5, m = 10
print(str(n) + " " + str(m))