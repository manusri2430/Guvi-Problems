n, m = [int(x) for x in raw_input().split(" ")]
print("even" if (n & 1 == 0 and m & 1 == 0) or (n & 1 != 0 and m & 1 != 0) else "odd")