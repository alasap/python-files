# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:23:07 2019

@author: Austin
"""
import numpy as np
import matplotlib.pyplot as pp
pp.style.use('seaborn')
pp.xlim(-0.1,5)
pp.ylim(0,9.2)
txtx=4.25
z=np.arange(-0.1,4.1,0.0001)
y=((np.tanh(z))*z)+z
y_=((1/np.tanh(z))*z)+z
y1=1*(z/z)
txty=1-.1
pp.plot(z,y1,':',color='k',alpha=1)
pp.text(txtx,txty,'\u03B1= $\\frac{\hbar^{2}}{2ma}$',fontsize=12)
y2=2*(z/z)
pp.plot(z,y2,':',color='k',alpha=0.9)
txty=2-.1
pp.text(txtx,txty,'\u03B1= $\\frac{\hbar^{2}}{ma}$',fontsize=12)
y4=4*(z/z)
pp.plot(z,y4,':',color='k',alpha=0.8)
txty=4-.1
pp.text(txtx,txty,'\u03B1= $\\frac{2\hbar^{2}}{ma}$',fontsize=12)
y8=8*(z/z)
pp.plot(z,y8,':',color='k',alpha=0.7)
txty=8-.1
pp.text(txtx,txty,'\u03B1= $\\frac{4\hbar^{2}}{ma}$',fontsize=12)
pp.xlabel('z')

pp.plot(z,y,'-',color='blue',alpha=0.6,label='$z(1+Tan(z))$')
pp.plot(z,y_,'-',color='green',alpha=0.5,label='$z(1+\\frac{1}{Tan(z)})$')
pp.legend(loc='upper center')
pp.title('Transcendental Equations(Double Dirac Well Bound State Solutions) \nFor varying \u03B1 values',color='steelblue',fontsize=15)
pp.tight_layout()
#pp.savefig('Double Dirac Well Varying Potentials',dpi=2000)
