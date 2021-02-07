
from math import exp,log,sqrt


import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from numpy.random import rand
from scipy.integrate import odeint
"""

k = 1.38064852e-23
T = float(300)

n = 100
Q = 0
Eav = 0
g = []
t = []
p = []
E = []
Esq = []
Esqav = 0

###########################

for i in range (0,100):
    n = float(i)
    g.insert(i , 2*n+1)
    t.insert(i , g[i] * exp( -2.3e-22*n*(n+1) / (k*T) ))
    Q = Q + t[i]

for i in range (0,100):
    n = float(i)
    p.insert(i, t[i]/Q)
    E.insert(i, 2.3e-22*n*(n+1)*t[i]/Q)
    Esq.insert(i, (2.3e-22*n*(n+1))**2 * t[i]/Q)
    
for i in range (0,100):
    Eav = Eav + E[i]
    Esqav = Esqav + Esq[i]

A = -k*T*log(Q)
S = (Eav - A)/T
varE = Esqav - Eav**2
Cv = varE/(k*T**2)
rltE = sqrt(varE)/Eav


###############################

for i in range (0,3):
    print "p[%d] = %f" %(i,p[i])

print 'Q = ', Q
print 'E_average = ', Eav
print 'A = ', A
print 'S = ', S
print 'E_variance = ', varE
print 'Cv = ', Cv
print 'E_relative = ', rltE

print k*T/(2.3e-22)


"""

########################
########################
########################
########################
########################



A = [5,1]
x = A[0]
y = A[1]

B = [x**2 + 1, 2]
C = np.vstack((A,B))

D = [[5,1],[0,0]]
print C
print D
