# Sort ascending and descending a dictionary by value

def sort_dic(x):
	return sorted(x.values())

def reverse_sort(d):
	return sorted(d.values(),reverse=True)

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sort_dic(d))

print(reverse_sort(d))
