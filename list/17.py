# generate and print a list of square numbers 1 to 30 exclude the first 5

def square():
	ans = [i**2 for i in range(1,31)]
	print(ans[5:])

square()
