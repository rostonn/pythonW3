# add two objects of type int

def add_int(n1,n2):
	if (type(n1) is int and type(n2) is int):
		return n1+n2
	else:
		return "Arguments must be integers"

print(add_int(5,100))
print(add_int(5.0,100))
print(add_int("Hello world",4))
