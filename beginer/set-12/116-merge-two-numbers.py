n, k = [int(x) for x in raw_input().split(" ")]

lenthOfK = len(str(k))
print(n * (10**lenthOfK) + k)