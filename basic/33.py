# Program to return sum of 3 integers if two values are equal return 0

def three_sum(n1,n2,n3):
	if n1 == n2 or n1 == n3 or n2 == n3:
		print("Zero Zero Zero")
		return 0
	else:
		print(n1+n2+n3)
		return n1+n2+n3

three_sum(1,2,3)
three_sum(1,1,3)
three_sum(1,1,1)
three_sum(1,2,1)
three_sum(2,1,1)
