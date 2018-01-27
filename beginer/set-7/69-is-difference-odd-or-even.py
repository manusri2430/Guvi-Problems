n, m = [int(x) for x in raw_input().split(" ")]
print("even" if (abs(n-m) & 1 == 0) else "odd")