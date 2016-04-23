# python function takes a list of words and returns the length of the longest

def return_longest_word(words):
	print(max(words))
	return len(max(words, key=len))

test = ["hello world","this", "isn;t andddddddddd"]

print(return_longest_word(test))

