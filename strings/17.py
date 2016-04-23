# get a string made of 4 copies of the last two characters of a specified string

def s_four(string):
	if len(string) < 3:
		return string
	return 4*string[-2:]

print(s_four("hello"))
print(s_four("go"))
