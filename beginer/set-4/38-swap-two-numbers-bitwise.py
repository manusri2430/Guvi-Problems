n, m = [int(x) for x in raw_input().split(" ")]
n = n ^ m
m = n ^ m
n = n ^ m
print(str(n) + " " + str(m))