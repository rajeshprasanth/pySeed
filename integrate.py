#!/usr/bin/env python

import functions
import matplotlib.pyplot as plt
import numpy as np

x,y = [],[]

test_x, test_y = [],[]

x = [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0]

x_l = 1.0
x_u = 5.0
n = 8

test_x = np.linspace(x_l,x_u,num=n+1)

for j in range(len(test_x)):
	test_y.append(functions.testfunc(test_x[j]))
	
#print test_x
#print test_y

functions.trapezoidal(test_x,test_y,8)
	
#for i in range(len(x)):
#	y.append(functions.logistic_1(A=24, B=0.5, C=100, x=x[i]))
#print "----"
#print (functions.trapezoidal(x,y,1))
#print "----"
#plt.plot(x, y)
#plt.show()
#print x,y
