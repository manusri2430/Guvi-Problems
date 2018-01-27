n = int(raw_input())
print("Yes" if n != 0 and (n & (n-1) ==0) else "No")