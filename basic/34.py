# sum two integers - if sum is between 15 and 20 return 20

def sum_two(n1,n2):
	sum = n1 + n2
	if sum > 14 and sum < 21:
		return 20
	return sum

print(sum_two(10,5))
print(sum_two(10,11))

