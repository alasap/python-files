# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 09:03:18 2019

@author: Austin
"""
import numpy as np
import matplotlib.pyplot as pp
from scipy.optimize import fsolve
z0=8
z=np.arange(0,z0+.1,0.001)
pp.style.use('seaborn')
cot=-(np.cos(z)/np.sin(z))
z[3141]=np.nan
z[6283]=np.nan
tan=np.sin(z)/np.cos(z)
z[1570]=np.nan
z[4712]=np.nan
z[7853]=np.nan
sqrt=np.sqrt(((z0/z)**2)-1)
pp.plot(z,(cot),':',color='b',label='-Cot(Z)')
pp.plot(z,(tan),':',color='green', label='Tan(Z)')
pp.plot(z,sqrt, color='r', label='$ \sqrt{\\frac{Z\o^{2}}{Z^{2}}-1}$' )
pp.ylim(0,z0)
pp.xlabel('Z')
pp.title('Plot of -Cot(Z) & Tan(Z) Vs. $\sqrt{\\frac{Z\o^{2}}{Z^{2}}-1}$\n(where V$\o$=$\\frac{\hbar^{2}}{ma^{2}}$ and Z$\o$=8)',fontsize=12,color='steelblue')
pp.xlim(0,z0+0.70)
functan = lambda z:np.sin(z)/np.cos(z)-np.sqrt(((z0/z)**2)-1)
funccot = lambda z:-(np.cos(z)/np.sin(z)+np.sqrt(((z0/z)**2)-1))
guess1=1
guess2=2.5
guess3=4
guess4=5.5
guess5=6.8
guess6=7.2
sol1= fsolve(functan,guess1)
sol2= fsolve(funccot,guess2)
sol3= fsolve(functan,guess3)
sol4= fsolve(funccot,guess4)
sol5= fsolve(functan,guess5)
sol6= fsolve(funccot,guess6)
tany1=np.tan(sol1)
tany3=np.tan(sol3)
tany5=np.tan(sol5)
coty2=-(1/np.tan(sol2))
coty4=-(1/np.tan(sol4))
coty6=-(1/np.tan(sol6))
e1=int((((sol1**2)/2)-32)*1000)/1000
e2=int((((sol2**2)/2)-32)*1000)/1000
e3=int((((sol3**2)/2)-32)*1000)/1000
e4=int((((sol4**2)/2)-32)*1000)/1000
e5=int((((sol5**2)/2)-32)*1000)/1000
e6=int((((sol6**2)/2)-32)*1000)/1000
pp.plot(sol1,tany1,'o',color='aqua',alpha=0.6,label='Z$\u2081$= '+str(int(sol1*1000)/1000))
pp.text(sol1+0.25,tany1,'E$\u2081$= '+str(e1)+' V$\o$')
pp.plot(sol2,coty2,'o',color='magenta',alpha=0.6,label='Z$\u2082$= '+str(int(sol2*1000)/1000))
pp.text(sol2+0.25,coty2,'E$\u2082$= '+str(e2)+' V$\o$')
pp.plot(sol3,tany3,'o',color='aqua',alpha=0.6,label='Z$\u2083$= '+str(int(sol3*1000)/1000))
pp.text(sol3+0.25,tany3,'E$\u2083$= '+str(e3)+' V$\o$')
pp.plot(sol4,coty4,'o',color='magenta',alpha=0.6,label='Z$\u2084$= '+str(int(sol4*1000)/1000))
pp.text(sol4+0.25,coty4,'E$\u2084$= '+str(e4)+' V$\o$')
pp.plot(sol5,tany5,'o',color='aqua', alpha=0.6,label='Z$\u2085$= '+str(int(sol5*1000)/1000))
pp.text(sol5+0.25,tany5+0.15,'E$\u2085$= '+str(e5)+' V$\o$')
pp.plot(sol6,coty6,'o',color='magenta',alpha=0.6,label='Z$\u2086$= '+str(int(sol6*1000)/1000))
pp.text(sol6-0.15,coty6+0.35,'E$\u2086$= '+str(e6)+' V$\o$')
pp.legend(loc='upper right')
pp.tight_layout()
#pp.savefig('Bound Even&Odd Finite Square Well Solutions.png',dpi=2500)



