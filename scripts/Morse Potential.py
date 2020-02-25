import numpy as np
from matplotlib import pyplot as pp
x=np.linspace(-7,6,10000)
pp.ylim(0,1.1)

x0=a=4
b=3
e=np.exp(-(b)*(x-a))
print(e)
v=(1/2)*((1-e)**2)
l=((x-a)**2)*(1/2)*(b**2)
pp.plot(x,v, color='b',label='\u03B2''=3')
pp.plot(x,l,':', color='b', alpha=0.6)

x0=a=2
b=2
e=np.exp(-(b)*(x-a))
print(e)
v=(1/2)*((1-e)**2)
l=((x-a)**2)*(1/2)*(b**2)
pp.plot(x,v, color='g',label='\u03B2''=2')
pp.plot(x,l,':',color='g',alpha=0.6)

x0=a=0
b=1
e=np.exp(-(b)*(x-a))
print(e)
v=(1/2)*((1-e)**2)
l=((x-a)**2)*(1/2)*(b**2)
pp.plot(x,v, color='r',label='\u03B2''=1')
pp.plot(x,l,':', color='r',alpha=0.6)

x0=a=-2
b=(7/8)
e=np.exp(-(b)*(x-a))
print(e)
v=(1/2)*((1-e)**2)
l=((x-a)**2)*(1/2)*(b**2)
pp.plot(x,v, color='purple',label='\u03B2''=0.875')
pp.plot(x,l,':', color='purple',alpha=0.6)

x0=a=-5
b=(5/8)
e=np.exp(-(b)*(x-a))
print(e)
v=(1/2)*((1-e)**2)
l=((x-a)**2)*(1/2)*(b**2)
pp.plot(x,v, color='orange',label='\u03B2''=0.625')
pp.plot(x,l,':', color='orange',alpha=0.6)

pp.title('Morse Potentials when ''\u03B1''=1'
         '\n With the Taylor Approximations')
pp.ylabel('V(x)')
pp.xlabel('x')
pp.legend()
pp.show()