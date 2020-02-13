
import numpy
from matplotlib import pyplot
from control.matlab import *


num1 = numpy.array([1])
den1 = numpy.array([1, 1])
G_1 = tf(num1, den1)
t=numpy.linspace(0,10,100)
y_1, t_1 =step(G_1,t)
y_1i, t_1i =impulse(G_1,t)

pyplot.figure()
pyplot.plot(t_1,y_1,label=r"$\frac{1}{s+1}$")
pyplot.xlabel(r"$t$ (sec)")
pyplot.title("Step Response")
pyplot.legend()
pyplot.grid()
pyplot.show()


pyplot.figure()
pyplot.plot(t_1i, y_1i, label=r'$\frac{1}{s+1}$')
pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.title('Impulse response')
pyplot.legend()
pyplot.grid()
pyplot.show()