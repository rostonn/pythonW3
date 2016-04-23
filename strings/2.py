# python program to count the number of characters in a string

def character_count(string):
	copy = string.replace(" ","")
	ans = {}
	for c in copy:
		ans[c] = copy.count(c)
	return ans
print("Hello the world")
print(character_count("hello the world"))

def char_cout(string):
	dict = {}
	for n in string:
		keys = dict.keys()
		print(keys)
		if n in keys:
			dict[n] += 1
		else:
			dict[n] = 1
	return dict

print(char_cout("hello the world"))	
