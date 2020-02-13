import numpy
from matplotlib import pyplot
from control.matlab import *

# 1/s^2+s+1
num = numpy.array([1])
den = numpy.array([1, 1, 1])
G_tf = tf(num, den)

print(G_tf)

t = numpy.linspace(0, 10, 100)

y_tf, t_tf = step(G_tf, t)

pyplot.figure()
pyplot.plot(t_tf, y_tf, label='TF')
pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
pyplot.show()