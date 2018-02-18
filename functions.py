#!/usr/bin/env python

import math

def logistic_1(A,B,C,x):
	y = C/ (1 + (A*math.exp((-B)*x)))
	return y
	
def trapezoidal(x,y,n):
	del_x = (x[len(x)-1] - x[0])/n
	l_extreme = y[0]
	u_extreme = y[len(y)-1]
	mid_term = 0
	print "-----"
	for i in range(1,(len(y)-1)):
		mid_term = mid_term + (2 * y[i])
	
	AUC = ((l_extreme + u_extreme + mid_term) * del_x )/2
	print AUC
 	return AUC
 	
def testfunc(x):
 	y = math.sqrt(1 + (x*x))
 	return y
