h1, m1 = [int(x) for x in raw_input().split(" ")]
h2, m2 = [int(x) for x in raw_input().split(" ")]

timeDiffInMinutes = abs((h1 * 60 + m1) - (h2 * 60 + m2))

print(str(timeDiffInMinutes / 60) +" "+ str(timeDiffInMinutes % 60))