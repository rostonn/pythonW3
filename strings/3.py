# return first two + last two chars of given string , if length less than two return empty string

def string_return(string):
	if len(string) < 2:
		return ''
	else:
		return string[:2]+string[-2:]

print(string_return("hello"))
print(string_return("d"))
print(string_return("boxifox"))
