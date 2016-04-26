# Check if a list is empty

def empty_list(x):
	if len(x) == 0:
		return True
	return False

print(empty_list([1,2,3]))
print(empty_list([]))
