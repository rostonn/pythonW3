# count the number of strings in a list where the length is 2 or more

def count_string(list):
	ans = 0
	for item in list:
		if type(item) is str and len(item) > 1:
			ans += 1
	return ans

print(count_string(['hello','i','am',132324]))

