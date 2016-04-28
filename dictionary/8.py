# merge two dictionaries

def merge_dic(d1,d2):
	a = d1.copy()
	print(a)
	a.update(d2)
	print(a)
	return(a)

d1 = {1:"ehhhe","there":44}
d2 = {11:"ehhhe","th1ere":455555}

print(merge_dic(d1,d2))
