def two_characters(string,n):
	if len(string) < 2:
		return string
	else:
		return n * string[0:2]

print(two_characters("jump",5))
print(two_characters("h",10))


