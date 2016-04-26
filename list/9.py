#Write a python program to clone or copy a list

def copy_list(x):
	n = x[:]
	return n

print(copy_list([1,2,3,4,5]))

