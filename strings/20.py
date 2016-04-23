# reverses a string if it's length is a multiple of 4

def four_r(string):
	if len(string) % 4 == 0:
		return string[::-1]
	return string

print(four_r("hell"))

