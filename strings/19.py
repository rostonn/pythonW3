# retrun first half of an length of an even string

def half(string):
	half = int(len(string)/2)
	return string[:half]

print(half("hellos"))
