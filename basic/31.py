# Compute the greatest common divisor of two integers

def greatest_common_divisor(n1,n2):
	if n1 < n2:
		smaller = n1
	else:
		smaller = n2

	while smaller > 1:
		if n1 % smaller == 0 and n2 % smaller == 0:
			return smaller
		smaller = smaller -1
	return 1

print("12 and 8")
print(greatest_common_divisor(12,8))
print("137 and 6809")
print(greatest_common_divisor(137,6809))

