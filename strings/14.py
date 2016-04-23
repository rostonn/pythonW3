# program accepts comma separated sequence of words as input prints out 
# unique words in alphabetical order

s = input("Enter a lsit of comma separated words: ")
list = s.split(',')
sort = sorted(list, key=str.lower)
print(sort)
print(','.join(sort))

