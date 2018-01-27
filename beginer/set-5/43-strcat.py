def myStrcat(s1, s2):
	s3 = ''
	for s in s1:
		s3 += s
	for s in s2:
		s3 += s

	return s3

s1, s2 = [x for x in raw_input().split()]

print(myStrcat(s1, s2))
