n = int(raw_input())

reversed = ''
while n > 0:
	reversed += str(n%10)
	n = n / 10

print(reversed)