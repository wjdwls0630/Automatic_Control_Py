import numpy
from matplotlib import pyplot
from control.matlab import *

A = numpy.array([[-1, -1], [1, 0]])
B = numpy.array([[1], [0]])
C = numpy.array([0, 1])
D = numpy.array([0])
G_ss = ss(A, B, C, D)

print(G_ss)

# 1/s^2+s+1
num = numpy.array([1])
den = numpy.array([1, 1, 1])
G_tf = tf(num, den)

t = numpy.linspace(0, 10, 100)

y_tf, t_tf = step(G_tf, t)
y_ss, t_ss = step(G_ss, t)

pyplot.figure()
pyplot.plot(t_tf, y_tf, label='TF')
pyplot.plot(t_ss, y_ss, '--', label='SS')
pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
pyplot.show()


print (ss2tf(G_ss))
print (tf2ss(G_tf))