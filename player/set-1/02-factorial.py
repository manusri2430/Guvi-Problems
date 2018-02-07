def fact(n):    
    return 1 if n == 0 else fact(n-1) * n

n = int(raw_input())

print fact(n)