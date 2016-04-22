# Test whether letter is a vowel

import re

def is_a_vowel(letter):
	if(re.match(r'[aeiouy]',letter)):
		return True
	else:
		return False

print(is_a_vowel("a"))
print(is_a_vowel("l"))
print(is_a_vowel("o"))

