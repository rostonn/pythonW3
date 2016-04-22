# Write a program to print the filename extension

filename = input("Filename please: ")
list = filename.split('.')
print(list[-1])

index = filename.index('.')
print(filename[index+1:])
