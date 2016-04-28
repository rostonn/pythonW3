# check if a key already exists in a dictionary

def key_check(d,key):
	if key in d:
		return True
	return False

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print(key_check(d,2))

print(key_check(d,9))

