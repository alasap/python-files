# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:11:30 2019

@author: Austin
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:30:40 2019

@author: Austin
"""
import numpy as np
import matplotlib.pyplot as pp
from scipy.optimize import fsolve

z0=100
z=np.linspace(0.01,15,100000)

s1=np.cos(z)/np.sin(z)
sqrt=np.sqrt(((z0/z)**2)-1)
pp.plot(z,(-s1),color='b',label='Cot(z)')
pp.plot(z,sqrt, color='r')
pp.ylim(0,z0/3)
pp.xlim(0,12)
func = lambda z:np.cos(z)/np.sin(z)+np.sqrt(((z0/z)**2)-1)
# Plot it

z1_initial_guess = 3
z1_solution = fsolve(func, z1_initial_guess)
z2_initial_guess =6
z2_solution = fsolve(func, z2_initial_guess)
z3_initial_guess =9
z3_solution = fsolve(func, z3_initial_guess)
sol1=-(np.cos(z1_solution)/np.sin(z1_solution))
sol2=-(np.cos(z2_solution)/np.sin(z2_solution))
sol3=-(np.cos(z3_solution)/np.sin(z3_solution))
z1=int(float(z1_solution)*1000)/1000
z2=int(float(z2_solution)*1000)/1000
z3=int(float(z3_solution)*1000)/1000
pp.plot(z1_solution,sol1,'o',color='orange',alpha=0.6,label=z1)
pp.plot(z2_solution,sol2,'o',color='green',alpha=0.6,label=z2)
pp.plot(z3_solution,sol3,'o',color='purple',alpha=0.6,label=z3)
pp.xlabel('Z')
pp.title('Transcendental Equation for Z\u03BF=100')
pp.legend(loc='best')
print(z1_solution,sol1)
#pp.savefig('Finite Square Well.png',dpi=1200)




