x, y = [int(x) for x in raw_input().split(" ")]
x = x ^ y
y = x ^ y
x = x ^ y
print(str(x) + " " + str(y))