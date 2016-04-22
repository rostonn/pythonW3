'''
Write a Python program which accepts a sequence of comma-separated numbers from
user and generate a list and a tuple with those numbers.
'''

values = input('Enter , separated values: ')
print(values)
list = values.split(',')
tuple = tuple(list)
print(tuple)
