import numpy
from matplotlib import pyplot
from control.matlab import *

num = numpy.convolve([1, 1], [1, 5])
num *= 16000
den = numpy.convolve([1, 0], [1, 0.1])
den = numpy.convolve(den, [1, 8])
den = numpy.convolve(den, [1, 20])
den = numpy.convolve(den, [1, 50])

G = tf(num, den)
print(G)
print(margin(G))

#bode(G, Hz=False)

print(rlocus(G, kvect=numpy.linspace(0, 5.075, 10000)))

#nyquist(G)

#pyplot.title("10-47_Bode")

pyplot.title("10-47_RLocus")
pyplot.xlim([-60, 30]), pyplot.ylim([-35, 35])

#pyplot.title("10-47_Nyquist")
#pyplot.xlim([-1, 1]), pyplot.ylim([-5, 5])

pyplot.show()