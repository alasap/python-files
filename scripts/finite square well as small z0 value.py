# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:14:20 2019

@author: Austin
"""

import numpy as np
from matplotlib import pyplot as pp
z0=np.pi/3
z=np.linspace(0,2,1000000)
s=(np.cos(z)/np.sin(z))
sqrt=np.sqrt(((z0/z)**2)-1)
pp.plot(z,-s,color='orange', label='-Cot(Z)')
pp.plot(z,sqrt, color='r',label='Sqrt((Z\u03BF/Z)^2-1)')
pp.show
pp.ylim(0,1)
pp.xlim(0,2)
pp.xlabel('Z')
pp.legend(loc='best')
pp.title('Finite Square Well (odd solutions) for Z\u03BF=pi/3')
pp.show()