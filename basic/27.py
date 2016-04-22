# write a program to concatenate all elements of a list into a string and print it

def concat_list(list):
	string = ''
	for item in list:
		string  = string + str(item)
	print(string)

	print(''.join(str(e) for e in list))

concat_list([1,2,3,'a','ee'])
