#remove the nth index character from a non empty string

def remove_nth_char(string,index):
	return string[:index] + string[index+1:]

print(remove_nth_char("hello",0))
print(remove_nth_char("hello",3))
print(remove_nth_char("hello",2))






