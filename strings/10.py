# change a given string to a new string where the first and last characters have been changed

def switch_first_last(string):
	if len(string) == 1:
		return string
	return string[-1] + string[1:-1] + string[0]

print(switch_first_last("fuck"))
print(switch_first_last("po"))
print(switch_first_last("p"))
