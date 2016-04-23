# return a string where all occurences of first charcater replaced with $ except first character

def dollar_replace(string):
	ans = string[1:]
	print(ans)
	ans = ans.replace(string[0],'$')
	ans = string[0] + ans
	return ans

test = dollar_replace("hehhooohhh");
print(test)
	
