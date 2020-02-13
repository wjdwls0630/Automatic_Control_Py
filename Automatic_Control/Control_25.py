import numpy
from matplotlib import pyplot
from control.matlab import *

num = numpy.convolve([53.9, 53.9], [1, 2])
den = numpy.convolve([1, 0, 0], [1, 3])
den = numpy.convolve(den, [1, 2, 25])

G = tf(num, den)
print(G)
print(margin(G))

bode(G, Hz=False)

#rlocus(G)

#nyquist(G)

pyplot.title("10-41_Bode_K=53.9")

#pyplot.title("10-41_RLocus")

#pyplot.title("10-41_Nyquist_K=53.9")
#pyplot.xlim([-10, 1]), pyplot.ylim([-5, 5])

pyplot.show()