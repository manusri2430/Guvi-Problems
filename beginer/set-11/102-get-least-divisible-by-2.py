def do_stuff(input):
	n = int(input)
	
	while n & 1 == 0:
		n = n >> 1
	print(n)
		

while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) # next line was found 
  except (EOFError):
    break #end of file reached