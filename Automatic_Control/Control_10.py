import numpy
from matplotlib import pyplot
from control.matlab import *

omega = 1
zeta = 0.7
num = numpy.array([1, 0, omega**2])
den = numpy.array([1, 2*zeta*omega, omega**2])
Gs = tf(num,den)

print(f'poles at {pole(Gs)}')
print(f'zeros at {zero(Gs)}')

t = numpy.linspace(0, 10, 100)
yy, tt = step(Gs)
pyplot.figure()
pyplot.plot(tt, yy, label='open loop')
pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.grid()
pyplot.show()
