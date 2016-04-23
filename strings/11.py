# remove the characters of a string with an odd index

def remove_odd_chars(string):
	ans = ''
	for i in range(0,len(string),2):
		print(i)
		ans += string[i]
	return ans

print(remove_odd_chars("012345678"))
print(remove_odd_chars("01234567"))


