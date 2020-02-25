# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:24:05 2019

@author: Austin
"""

import numpy as np
from matplotlib import pyplot as pp
B1= np.array([[30,0],[75,0.1],[150,0.2],[255,0.3],[315,0.4],[495,0.5],[555,0.6],
               [600,0.7],[705,0.8],[840,0.9],[900,1],[960,1.1],[1020,1.2],[1080,1.3],
               [1185,1.4],[1260,1.5],[1320,1.5],[1410,1.6],[1530,1.8],[1605,1.9],[1665,2],
               [1770,2.1],[1890,2.3],[2010,2.5],[2100,2.6],[2190,2.7],[2310,2.8]])

x1=B1[:,0]
y1=B1[:,1]

z1= np.polyfit(x1,y1,1)

x= B1[:,0]
yb1= z1[0]*x+z1[1]


pp.plot(x1,y1,':',color=('g'), label='Band 1')
pp.title('Band 1 Position')
pp.xlabel('Time(s)')
pp.ylabel('Position(cm)')
pp.legend()

pp.title('Band 1 Line of Best Fit')
pp.xlabel('Time(s)')
pp.ylabel('Position(cm)')
pp.plot(x,yb1,'-', color=('g'), label='Line of Best Fit')
pp.legend()
print(z1)
pp.show()
