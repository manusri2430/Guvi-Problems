def isLeapYear(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return "Yes"
			else:
				return "No"
		else:
			return "Yes"
	else:
		return "No"

year = int(raw_input())
print(isLeapYear(year))