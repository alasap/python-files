# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:38:52 2019

@author: Austin
"""

import numpy as np
from matplotlib import pyplot as pp
B2= np.array([[30,0],[75,0.1],[150,0.2],[255,0.3],[315,0.4],[495,0.5],[555,0.6],
               [600,0.7],[705,0.8],[840,1],[900,1.1],[960,1.2],[1020,1.3],[1080,1.4],
               [1185,1.5],[1260,1.6],[1320,1.6],[1410,1.7],[1530,2.0],[1605,2.1],[1665,2.2],
               [1770,2.3],[1890,2.5],[2010,2.7],[2100,2.8],[2190,2.9],[2310,3.0]])
x1=B2[:,0]
y1=B2[:,1]

z1= np.polyfit(x1,y1,1)

x= B2[:,0]
yb1= z1[0]*x+z1[1]


pp.plot(x1,y1,':',color=('red'), label='Band 2')
pp.title('Band 2 Position')
pp.xlabel('Time(s)')
pp.ylabel('Position(cm)')
pp.legend()

pp.title('Band 2 Line of Best Fit')
pp.xlabel('Time(s)')
pp.ylabel('Position(cm)')
pp.plot(x,yb1,'-', color=('red'), label='Line of Best Fit')
print(z1)
pp.legend()
pp.show()