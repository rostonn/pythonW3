# write a program to get a single string from two given strings separated bya space and swap 
# the first two characters of each string

def swap_return(s1,s2):
	s1ans = s2[:2]
	s2ans = s1[:2]
	s1ans += s1[2:]
	s2ans += s2[2:]
	return s1ans + ' ' + s2ans

print(swap_return("hi","bye"))
