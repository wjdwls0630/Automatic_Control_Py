import numpy
from matplotlib import pyplot
from control.matlab import *

num1 = numpy.array([100])
den1 = numpy.array([1, 100])
num2 = numpy.array([4])
den2 = numpy.array([1, 2, 4])

G_1 = tf(num1, den1)
G_2 = tf(num2, den2)

t = numpy.linspace(0,30, 100)

y_result, t_result = step(G_1*G_2, t)
pyplot.figure()
pyplot.plot(t_result, y_result, label="TF")
pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
pyplot.show()