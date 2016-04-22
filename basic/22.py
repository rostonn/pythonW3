def number_four(list):
	counter = 0
	for num in list:
		if num == 4:
			counter = counter + 1
		
	return counter

list = [4,5,6,7,4,4,4]

print(number_four(list))

