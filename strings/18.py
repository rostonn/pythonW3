# return first three characters if the string is 3 or less return the string

def s3(string):
	if len(string) < 4:
		return string
	return string[:3]

print(s3("hellooo"))

