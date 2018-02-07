s = raw_input()

r=''
for i in range(len(s), 0, -1):
	r += s[i - 1]

print(r)