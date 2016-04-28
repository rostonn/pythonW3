# Write a program to add a key to a dictionary

def add_key(d,value):
	key = len(d.values())
	d[key] = value
	return d

d = {0:10,1:20}

print(add_key(d,5000))
