# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:06:15 2019

@author: Austin
"""

import matplotlib.animation as animation
from matplotlib import pyplot as pp
import numpy as np
a=4
n1=1
n2=5
c1=3/5
c2=2/5

# First set up the figure, the axis, and the plot element we want to animate
fig = pp.figure()
ax = pp.axes(xlim=(0, 10), ylim=(-0.01, 0.01))
line, = ax.plot([], [], lw=2)
line1, =ax.plot([],[],lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    line1.set_data([], [])
    return line,line1



# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 10, 1000)
    y = ((np.sqrt(2/a)*np.sqrt(c1))*np.sin(n1*(np.pi * (x - 0.01*i))/a)*np.exp((-0.0015*i)*(n1**2))+(np.sqrt(2/a)*np.sqrt(c2))*np.sin((n2 * np.pi * (x - 0.01*i))/a)*np.exp((-0.0015*i)*(n2**2)))*((np.sqrt(2/a)*np.sqrt(c1))*np.sin(n1*(np.pi * (x - 0.01*i))/a)*np.exp((0.0015*i)*(n1**2))+(np.sqrt(2/a)*np.sqrt(c2))*np.sin((n2 * np.pi * (x - 0.01*i))/a)*np.exp((0.0015*i)*(n2**2)))
    y2=((np.sqrt(2/a)*np.sqrt(c1))*np.sin(n1*(np.pi * (x - 0.01*i))/a)*np.exp((-0.0015*i)*(n1**2))+(np.sqrt(2/a)*np.sqrt(c2))*np.sin((n2 * np.pi * (x - 0.01*i))/a)*np.exp((-0.0015*i)*(n2**2)))
    line.set_data(x,y)
    line1.set_data(x,y2)
    return line,line1

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate,init_func=init,
                               frames=2000, interval=20, blit=True)
#anim = animation.FuncAnimation(fig, animate1, init_func=init1,
                               #frames=200, interval=20, blit=True)
#anim.save('my_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
pp.show



