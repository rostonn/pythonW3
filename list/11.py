# take two lists, return true if there is at least one common member

def common(l_1,l_2):
	for char1 in l_1:
		for char2 in l_2:
			if char1 == char2:
				return True
	return False

print(common([1,2,3],[1,4,5]))
print(common([1,2,3],[0,4,5]))
