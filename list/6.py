# Program to sort list of tuples by the second tuple value

def sort_t(list):

	ans = []
	for i in range(len(list)):
		for j in range(len(list)-1):
			if list[j][1] > list[j+1][1]:
				temp = list[j]
				list[j] = list[j+1]
				list[j+1] = temp
	return list

sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(len(sample))
print(sort_t(sample))
		
