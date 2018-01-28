def do_stuff(input):
	x, op, y = [x for x in input.split(" ")]
	if op == '/':
		print(int(x) / int(y))
	else:
		print(int(x) % int(y))
		

while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) # next line was found 
  except (EOFError):
    break #end of file reached