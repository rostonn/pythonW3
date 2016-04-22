# Least common multiple

def lcm(n1,n2):
	if n1 > 2:
		start = n1
	else:
		start = n2
	while start < n1*n2:
		if start % n1 == 0 and start % n2 == 0:
			return start
		start += 1
	return n1*n2

print(lcm(4,8))
print(lcm(89,5764))

