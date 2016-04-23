# add 'ing' at the end of a given string length should be at least 3
# if a given string ends with 'ing' add 'ly' instead
# if the string length is less than three, leave it unchanged

def return_ing(string):
	if len(string) < 3:
		return string
	if string[-3:] == 'ing':
		return string + 'ly'
	else:
		return string + 'ing'

print(return_ing("hello"))
print(return_ing("is"))
print(return_ing("fucking"))

