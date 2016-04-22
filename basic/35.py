# Write program that returns true if two integers are equal or their sum or difference is 5

def sum_two(n1,n2):
	if n1 == n2:
		return True
	elif n1 + n2 == 5 or n1-n2 ==5 or n2-n1==5:
		return True
	else:
		return False

print(sum_two(1,4))
print(sum_two(1,1))
print(sum_two(6,1))
print(sum_two(1,6))
