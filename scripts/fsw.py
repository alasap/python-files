# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 09:03:18 2019

@author: Austin
"""
import numpy as np
import matplotlib.pyplot as pp
from scipy.optimize import fsolve
z0=2
z02=10
z=np.arange(0,z02+.1,0.001)
pp.style.use('seaborn')

functan = lambda z:-(np.tan(z))-(1/(np.sqrt(((z0/z)**2)-1)))
functan2 = lambda z:-(np.tan(z))-(1/(np.sqrt(((z02/z)**2)-1)))
if z0>1.5:
  z[1570]=np.nan
  guess1=float(np.pi/2)+0.01
  sol1= fsolve(functan,guess1)
  y1=-np.tan(sol1)
  pp.plot(sol1,y1,'o')
  pp.text(sol1+0.1,y1+0.1,'z='+str(sol1))
if z0>4.5:
  z[4712]=np.nan
  guess2=5.5
  sol2=fsolve(functan,guess2)
  y2=-np.tan(sol2)
  pp.plot(sol2,y2,'o')
  pp.text(sol2+0.1,y2+0.1,'z='+str(sol2))
if z0>7.5:
  z[7853]=np.nan
  guess3=8.5
  sol3=fsolve(functan,guess3)
  y3=-np.tan(sol3)
  pp.plot(sol,y3,'o')
  pp.text(sol3+0.1,y3+0.1,'z='+str(sol3))
if z0>10.5:
  z[1100]=np.nan


if z02>1.5:
  z[1570]=np.nan
  guess4=float(np.pi/2)+0.01
  sol4= fsolve(functan2,guess4)
  y4=-np.tan(sol4)
  pp.plot(sol4,y4,'o')
  pp.text(sol4+0.1,y4-0.1,'z='+str(sol4))
if z02>4.5:
  z[4712]=np.nan
  guess5=5.5
  sol5=fsolve(functan2,guess5)
  y5=-np.tan(sol5)
  pp.plot(sol5,y5,'o')
  pp.text(sol5+0.1,y5-0.1,'z='+str(sol5))
if z02>7.5:
  z[7853]=np.nan
  guess6=8.5
  sol6=fsolve(functan2,guess6)
  y6=-np.tan(sol6)
  pp.plot(sol6,y6,'o')
  pp.text(sol6+0.1,y6-0.1,'z='+str(sol6))
if z02>10.5:
  z[1100]=np.nan


LHS=-(np.tan(z))

RHS=1/(np.sqrt(((z0/z)**2)-1))
RHS2=1/(np.sqrt(((z02/z)**2)-1))

pp.plot(z,(LHS),':',color='green', label='-Tan(Z)')
pp.plot(z,RHS, color='r', label='$ \\frac{1}{\sqrt{\\frac{'+str(z0)+'^{2}}{Z^{2}}-1}}$' )
pp.plot(z,RHS2, color='b', label='$ \\frac{1}{\sqrt{\\frac{'+str(z02)+'^{2}}{Z^{2}}-1}}$' )
pp.xlabel('Z',fontsize=12)
pp.xticks(fontsize=15)
pp.yticks(fontsize=15)
txt=('Plot of -Tan(Z) Vs. $\\frac{1}{\sqrt{\\frac{Z\o^{2}}{Z^{2}}-1}}$\n(where Z$\o$='+str(z0)+' & '+str(z02)+')')
pp.title(txt,fontsize=15,color='black')

pp.legend(loc='best',fontsize=15)
pp.tight_layout()
pp.xlim(0,z02)
pp.ylim(0,y1+0.2)
#pp.show()
pp.savefig('Finite Spherical Well.pdf',dpi=2500)
