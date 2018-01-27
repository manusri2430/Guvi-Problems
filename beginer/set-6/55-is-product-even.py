x, y = [int(x) for x in raw_input().split(" ")]
print("even" if (x & 1 == 0 or y & 1 == 0) else "odd")