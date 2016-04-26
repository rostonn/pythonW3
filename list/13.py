# generate a 3*4*6 3D array where each element is *

def big_array():
	ans = []
	for i in range(3):
		for j in range(4):
			for k in range(6):
				ans[i][j][k] = '*'
	return ans

def b_arr():
	array = [[['*' for col in range(6)] for col in range(4)] for col in range(3)]
	return array

print(b_arr())
