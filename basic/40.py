# compute distance between (x1,y1) and (x2,y2)
import math
def distance(x1,y1,x2,y2):
	x = (abs(x2-x1))**2
	y = (abs(y2-y1))**2
	d = math.sqrt(x + y)
	return d

print(distance(5,5,10,10))
