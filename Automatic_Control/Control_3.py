import numpy
from matplotlib import pyplot
from control.matlab import *

# 1/s+1
num1 = numpy.array([1])
den1 = numpy.array([1, 1])
G_1 = tf(num1, den1)

# 2/s+2
num2 = numpy.array([2])
den2 = numpy.array([1, 2])
G_2 = tf(num2, den2)

# 1/s+2
num3 = numpy.array([1])
den3 = numpy.array([1, 2])
G_3 = tf(num3, den3)

t = numpy.linspace(0, 10, 100)

y_1, t_1 = step(G_1, t)
y_2, t_2 = step(G_2, t)
y_3, t_3 = step(G_3, t)

pyplot.figure()
pyplot.plot(t_1, y_1, label=r'$\frac{1}{s+1}$')
pyplot.plot(t_2, y_2, label=r'$\frac{2}{s+2}$')
pyplot.plot(t_3, y_3, label=r'$\frac{1}{s+2}$')
pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
pyplot.show()
