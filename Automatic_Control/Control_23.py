import numpy
from matplotlib import pyplot
from control.matlab import *

num = numpy.convolve([1, 5], [1, 1])
den = numpy.convolve([1, 2], [1, 2])
den = numpy.convolve(den, [1, 2])
den = numpy.convolve(den, [1, 50])


G = tf(num, den)
print(G)

#bode(G, Hz=False)

rlocus(G)

#nyquist(G)

#pyplot.title("10-16.(e)_Bode")

pyplot.title("10-16.(e)_RLocus")

#pyplot.title("10-16.(e)_Nyquist")
#pyplot.xlim([-1, 0.4]), pyplot.ylim([-0.01, 0.01])

pyplot.show()