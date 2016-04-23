# Write a Python function to create the HTML string with tags around the words

def add_tags(tag,str):
	front_tag = '<'+tag+'>'
	end_tag = '</'+tag+'>'
	return front_tag+str+end_tag

print(add_tags('h1',"Noah's Website"))
