def fact(n):
    if n == 0:
        return 1
    else:
        x = fact(n-1) * n
        return x

n = int(raw_input())

print fact(n)