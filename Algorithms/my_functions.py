import random
import math

def isPartOf(sub,whole):
# print(sub,'\n',whole)
	found = False
	for i in range(len(whole)-len(sub)+1):
		for j in range(len(sub)):
			if whole[i+j] == sub[j]:
				found = True
			else:
				found = False
				break
		if found:
			return i
	return -1


def rand():
	if random.random() >= 0.5:
		return 1
	else:
		return 0

def inCircle(x,y,r):
	if math.sqrt(x*x+y*y) <= r:
		return True
	else:
		return False
