# Program that multiplies all of the items in a list

def multiply(list):
	ans = 1
	for item in list:
		ans *= item
	return ans

print(multiply([1,2,4]))

