import numpy
from matplotlib import pyplot
from control.matlab import *

num = numpy.array([0.06, 0.75, 0])

den = numpy.array([3, 37.5, 0, 5000])

G = tf(num, den)
print(G)

pyplot.figure(dpi=100)
rlocus(G, xlim=[-20, 5], ylim=[-15, 15], Plot=True)
pyplot.title("9-31.(c)")
pyplot.grid()
pyplot.show()

