n = int(raw_input())
values = [int(x) for x in raw_input().split(" ")]

for i in range(len(values) - 1):
	if (values[i+1] < values[i]):
		print(values[i-1] + 1)
		break;
