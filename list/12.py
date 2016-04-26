# print a list after removing the 0th 2nd 4th and 5th elements

def remove_index(L):
	#remove 5th element
	del L[4]
	del L[3]
	del L[1]
	del L[0]
	return L

print(remove_index([0,1,2,3,4,5,6]))
s = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(['Green', 'White', 'Black'])
print(remove_index(s))
