import numpy
from matplotlib import pyplot
from control.matlab import *

num = numpy.array([1])

den = numpy.array([1, 2, 3, 2, 1, 0])

G = tf(num, den)

pyplot.figure(dpi=100)
rlocus(G, xlim=[-10, 10], ylim=[-15, 15], Plot=True)
pyplot.title("9-14.(k)")
pyplot.grid()
pyplot.show()

