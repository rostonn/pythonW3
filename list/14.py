# Print numbers of a list after removing the even numbers

def remove_even(x):
	ans = []
	for num in x:
		if num % 2 != 0:
			ans.append(num)
	return ans

print(remove_even([1,2,3,4,5,6,7,8,9]))
