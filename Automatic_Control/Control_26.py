import numpy
from matplotlib import pyplot
from control.matlab import *

num = numpy.convolve([0.2, 1], [0.1, 1])
num *= 7079
den = numpy.convolve([1, 0, 0], [1, 1])
den = numpy.convolve(den, [0.01, 1])
den = numpy.convolve(den, [0.01, 1])

G = tf(num, den)
print(G)
print(margin(G))

bode(G, Hz=False)

#rlocus(G)

#nyquist(G)

pyplot.title("10-45_Bode_K=7079")

#pyplot.title("10-45_RLocus")
#pyplot.xlim([-120, 60])

#pyplot.title("10-41_Nyquist_K=53.9")
#pyplot.xlim([-1, 1]), pyplot.ylim([-5, 5])

pyplot.show()