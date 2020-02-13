import numpy
from matplotlib import pyplot
from control.matlab import *

# 1/s+1
num1 = numpy.array([1])
den1 = numpy.array([1, 1])
G_1 = tf(num1, den1)

K = 2
G_f = feedback(G_1, K, -1)
G_f = (1/dcgain(G_f))*G_f
print(G_f)

t = numpy.linspace(0, 10, 100)
y_1, t_1 = step(G_1, t)
y_f, t_f = step(G_f, t)

pyplot.figure()
pyplot.plot(t_1, y_1, label='open loop')
pyplot.plot(t_f, y_f, label='closed loop')
pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
pyplot.show()