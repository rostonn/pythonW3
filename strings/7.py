#the first appearance of the substring 'not' and 'poor' from a given string, 
#if 'bad' follows ithe 'poor', replace the whole 'not'...'poor' substring with 'good'. 

def sub_replace(string):
	index = string.find("not")
	poor = string.find("poor")
	if index < poor:
		return string[:index]+ "good"
	else:
		return string

print(sub_replace("it is not that very well poor"))

