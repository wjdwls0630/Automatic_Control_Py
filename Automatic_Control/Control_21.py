import numpy
from matplotlib import pyplot
from control.matlab import *

num = numpy.array([1, 0])

den = numpy.array([1, 5, 0, 10])

G = tf(num, den)

pyplot.figure(dpi=100)
rlocus(G, xlim=[-7, 3], ylim=[-15, 15], Plot=True)
pyplot.title("9-24.(b)")
pyplot.grid()
pyplot.show()

