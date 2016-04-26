# return a list from a given string of the words that are longer than n

def string_list(str,n):
	ans = str.split(' ')
	print(ans)
	real_answer = []
	for word in ans:
		if len(word) > n:
			real_answer.append(word)
	return real_answer
print(string_list("Hello world I am",3))

