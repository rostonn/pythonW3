# Write a function to insert a string in the middle of a string

def insert_middle(string,mid):
	middle = int(len(string)/2)
	beg = string[:middle]
	end = string[middle:]
	return beg+mid+end

print(insert_middle('{{}}','Python'))
print(insert_middle('<<>>','Python'))

print(insert_middle('{{{}}','Python'))
