# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:33:18 2019

@author: Austin
"""

import numpy as np
from matplotlib import pyplot as pp
B1= np.array([[144.465,0.00123169],[115.049,0.00134638],[49.026,0.00162924]])

x1=B1[:,0]
y1=B1[:,1]

z1= np.polyfit(x1,y1,2)


yb1= (z1[0]*x**2)+(z1[1]*x)+z1[2]


pp.plot(x1,y1,':',color=('g'), label='V-vs-MM')
pp.title('Velocity vs Molar-Mass')
pp.xlabel('Molar-Mass(Kg/mol)')
pp.ylabel('Velocity')
pp.legend()


print(z1)
pp.show()

mae=(1/27)*()