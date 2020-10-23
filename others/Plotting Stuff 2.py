from __future__ import division

from math import exp,log,sqrt,floor


import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from numpy.random import rand
from scipy.integrate import odeint


#################
## Define Constant

q0 = 0.5
p0 = 0.4

a = 1.0
b = 2.0
c = -1.0

n = 20



##################
## Define Matrix

A = np.array([[1,1],[1,2]])

Z = np.array([[q0],[p0]])

print Z


###################
## Iterations

for i in range (1,n):
    
    Z = np.dot(A,Z)
    
    if Z[0,0] > 1:
        alpha = floor (Z[0,0])
        Z[0,0] = Z[0,0] - alpha
    
    if Z[1,0] > 1:
        beta = floor (Z[1,0])
        Z[1,0] = Z[1,0] - beta

    print Z

       
    
