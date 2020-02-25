# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:30:40 2019

@author: Austin
"""
import numpy as np
import matplotlib.pyplot as pp
from scipy.optimize import fsolve

z0=8
z1=np.linspace(0.1,3.11,1000)
z2=np.linspace(3.17,6.2,1000)
z3=np.linspace(6.4,z0+1,1000)
z=np.linspace(0.1,z0,1000)

s1=np.cos(z1)/np.sin(z1)
s2=np.cos(z2)/np.sin(z2)
s3=np.cos(z3)/np.sin(z3)
sqrt=np.sqrt(((z0/z)**2)-1)
pp.plot(z1,(-s1),color='b',label='-Cot(Z)')
pp.plot(z2,(-s2),color='b')
pp.plot(z3,(-s3),color='b')
pp.plot(z,sqrt, color='r', label='$ \sqrt{\\frac{Zo^{2}}{Z^{2}}-1}$' )
pp.ylim(0,3)
func = lambda z:np.cos(z)/np.sin(z)+np.sqrt(((z0/z)**2)-1)
# Plot it

z1_initial_guess = 2.7
z1_solution = fsolve(func, z1_initial_guess)
z2_initial_guess = 5.5
z2_solution = fsolve(func, z2_initial_guess)
z3_initial_guess = 7.9
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
pp.xlabel('z')
pp.title('Plot of $ \sqrt{\\frac{Zo^{2}}{Z^{2}}-1}$ & -Cot(Z)')
pp.legend()
pp.show()
#pp.savefig('Finite Square Well.png',dpi=1200)




