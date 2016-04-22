number = int(input("Enter a number : "))
if number > 17:
	print(abs(2*(number - 17)))
else:
	print(abs(number - 17))

def difference(n):
	if n <= 17:
		return 17 - n
	else:
		return (n-17)*2

print(difference(22))
print(difference(14))

