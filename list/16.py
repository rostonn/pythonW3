# generate and print a list of first and last 5 elements where the values
# are square numbers between 1 and 30

def square():
	ans = []
	for i in range(1,6):
		ans.append(i**2)
	for i in range(25,30):
		ans.append(i**2)
	print(len(ans))
	print(ans)

square()
