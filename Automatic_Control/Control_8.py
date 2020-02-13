import numpy
from matplotlib import pyplot
from control.matlab import *

omega = 1
zeta = numpy.linspace(0, 1, 11)
t = numpy.linspace(0, 30, 100)

numpy.set_printoptions(precision=1)
pyplot.figure(figsize=(9,6))
for z in zeta:
  num = omega**2
  den = numpy.array([1, 2*z*omega, omega**2])
  Gs = tf(num,den)
  ys, ts = step(Gs, t)
  pyplot.plot(ts, ys, label=rf'$\zeta$={z:3.1f}')
pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
pyplot.show()