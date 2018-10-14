import random
import math

def monteCarlo(k):
	numOfOne = 0
	for n in range(1,k):
		numOfOne = numOfOne + rand()
		print(n, ": ",float(numOfOne / n))

def monteCarlo2(k):
	pointInCircle = 0
	for i in range(1,k):
		if(inCircle(random.random(),random.random(),1)):
			pointInCircle = pointInCircle + 1
		print(i," | Estimate value of Pi: ", 4*pointInCircle/i)