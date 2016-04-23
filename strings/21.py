# Convert a string to all uppercase if the string contains at least two uppercase characters
# in the first four characters

def upper(string):
	count = 0
	for i in range(0,4):
		if string[i].isupper():
			count += 1
	if count >= 2:
		return string.upper()
	return string

print(upper("HEllo"))
print(upper("hhhhHHHHHH"))


