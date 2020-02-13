import numpy
from matplotlib import pyplot
from control.matlab import *

# 1/s+1
num1 = numpy.array([1])
den1 = numpy.array([1, 1])
G1 = tf(num1, den1)

num2 = numpy.array([100])
den2 = numpy.array([1, 100])
G2 = tf(num2, den2)

num3 = numpy.array([10000])
den3 = numpy.array([1, 2*0.1*100, 10000])
G3 = tf(num3, den3)

t = numpy.linspace(0, 0.5, 100)
y_1, t_1 = step(G1*G2, t)
y_2, t_2 = step(G2, t)
y_3, t_3 = step(G1*G3, t)

pyplot.figure(dpi=100)
pyplot.plot(t_1, y_1, label="Full_1", alpha=0.8)
pyplot.plot(t_2, y_2, label="Reduced", alpha=0.8)
pyplot.plot(t_3, y_3, label="Full_2", alpha=0.8)
pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
pyplot.show()






