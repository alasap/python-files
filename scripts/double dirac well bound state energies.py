# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:10:11 2019

@author: Austin
"""
import numpy as np
import matplotlib.pyplot as pp
pp.style.use('seaborn')
pp.title('Even & Odd Bound State Energies for the Double Dirac well \nFor \u03B1= $\\frac{\hbar^{2}}{2ma},\\frac{\hbar^{2}}{ma}$ and V$\o=\\frac{\hbar^{2}}{ma}$',color='steelblue',fontsize=12)
func1 = lambda z:z*np.tanh(z)+z-1
func_1= lambda z:z*(1/np.tanh(z))+z-1
func2 = lambda z:z*np.tanh(z)+z-2
func_2 = lambda z:z*(1/np.tanh(z))+z-2
txtx=1.75
z=np.arange(-0.1,2,0.001)
y=((np.tanh(z))*z)+z
y_=((1/np.tanh(z))*z)+z
y1=1*(z/z)
y2=2*(z/z)
pp.plot(z,y,color='blue',label='$z(1+Tan(z))$')
pp.plot(z,y_,color='green',label='$z(1+\\frac{1}{Tan(z)})$')
pp.plot(z,y1,':',color='grey')
txty=1.1
pp.text(txtx,txty,'\u03B1= $\\frac{\hbar^{2}}{2ma}$',fontsize=11)
pp.plot(z,y2,':',color='grey')
txty=2.1
pp.text(txtx,txty,'\u03B1= $\\frac{\hbar^{2}}{ma}$',fontsize=11)
from scipy.optimize import fsolve
guess1=0
sol1=fsolve(func_1,guess1)
e1=(sol1**2)/2
txty=0.8
pp.text(sol1,txty,'E$\u2081$= '+str(int(e1))+'V$\o$',fontsize=10)
pp.plot(sol1,1,"o",alpha=0.6,label='$Z\u2081=$'+str(sol1))
guess1=0
sol2=fsolve(func1,guess1)
e2=int((-(sol2**2)/2)*1000)/1000
txty=0.8
pp.text(sol2,txty,'E$\u2082$= '+str(e2)+'V$\o$',fontsize=10)
pp.plot(sol2,1,"o",alpha=0.6,label='$Z\u2082=$'+str(sol2))
guess1=0.1
sol3=fsolve(func_2,guess1)
e3=int((-(sol3**2)/2)*1000)/1000
txty=2.05
pp.text(sol3-.3,txty,'E$\u2083$= '+str(e3)+'V$\o$',fontsize=10)
pp.plot(sol3,2,"o",alpha=0.6,label='$Z\u2083=$'+str(sol3))
guess1=0.1
sol4=fsolve(func2,guess1)
e4=int((-(sol4**2)/2)*1000)/1000
txty=2.05
pp.text(sol4+.1,txty,'E$\u2084$= '+str(e4)+'V$\o$',fontsize=10)
pp.plot(sol4,2,"o",alpha=0.6,label='$Z\u2084=$'+str(sol4))
pp.legend(fontsize=10)
#pp.savefig('Bound State Solutions for Double Dirac Well.png',dpi=2000)