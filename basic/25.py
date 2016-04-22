def check_value(list,value):
	if value in list:
		return True
	else:
		return False

print(check_value([1,2,3,4],1))
print(check_value([1,2,3,4],8))

