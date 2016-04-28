# Concat dictionaries to create a new one

def concat_dic(d1,d2,d3):
	d1.update(d2)
	d1.update(d3)
	return d1

dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}

print(concat_dic(dic1,dic2,dic3))
