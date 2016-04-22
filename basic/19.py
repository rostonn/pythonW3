#Write a Python program to get a new string from a given string where "Is" has been added to the front#. If the given string already begins with "Is" then return the

def string_return(string):
	s = string.lower()
	if s[0:2] == "is":
		return string
	else:
		return "Is " + string


print(string_return("Is this right?"))
print(string_return("That is correct")) 
