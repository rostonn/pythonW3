# Write a Python Program to test whether a number is within 100 if 1000
# or 2000

def thousand_test(num):
	if num > 2000:
		if (num - 100) < 2000:
			return True
		else:
			return False
	elif num < 2000 and num > 1000:
		if (num + 100) > 2000:
			return True
		elif (num - 100) < 1000:
			return True
		else:
			return False
	else:
		if(num + 100) > 1000:
			return True
		else:
			return False

print(thousand_test(100))
print(thousand_test(901))
print(thousand_test(2001))

 
