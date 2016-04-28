# dictionary in the form 1 to n (x, x*x)

def square(n):
	ans = {}
	for x in range(1,n):
		ans[x] = x**2
	print(ans)

square(6)
