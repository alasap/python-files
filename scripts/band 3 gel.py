# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:40:30 2019

@author: Austin
"""

import numpy as np
from matplotlib import pyplot as pp
B3= np.array([[30,0],[75,0.1],[150,0.2],[255,0.4],[315,0.5],[495,0.7],[555,0.8],
               [600,0.9],[705,1.1],[840,1.3],[900,1.4],[960,1.5],[1020,1.6],[1080,1.7],
               [1185,1.9],[1260,2],[1320,2.1],[1410,2.3],[1530,2.5],[1605,2.6],[1665,2.7],
               [1770,2.8],[1890,3.0],[2010,3.2],[2100,3.4],[2190,3.5],[2310,3.7]])
x1=B3[:,0]
y1=B3[:,1]

z1= np.polyfit(x1,y1,1)

x= B3[:,0]
yb1= z1[0]*x+z1[1]


pp.plot(x1,y1,':',color=('blue'), label='Band 3')
pp.title('Band 3 Position')
pp.xlabel('Time(s)')
pp.ylabel('Position(cm)')
pp.legend()

pp.title('Band 3 Line of Best Fit')
pp.xlabel('Time(s)')
pp.ylabel('Position(cm)')
pp.plot(x,yb1,'-', color=('blue'), label='Line of Best Fit')
print(z1)
pp.legend()
pp.show()