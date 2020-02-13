import numpy
from matplotlib import pyplot
from control.matlab import *

num = numpy.array([25, 25])
den = numpy.convolve([1, 0], [1, 2])
den = numpy.convolve(den, [1, 2, 16])

G = tf(num, den)
print(G)
print(margin(G))

#bode(G, Hz=False)

#rlocus(G)

nyquist(G)

#pyplot.title("10-37_Bode")

#pyplot.title("10-37_RLocus")

pyplot.title("10-37_Nyquist")
pyplot.xlim([-1, 0.4]), pyplot.ylim([-10, 10])

pyplot.show()