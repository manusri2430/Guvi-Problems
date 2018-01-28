n = int(raw_input())
l, r = [int(x) for x in raw_input().split(" ")]
print("Yes" if (n > l and n < r) else "No")