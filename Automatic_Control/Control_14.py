import numpy
from matplotlib import pyplot
from control.matlab import *

t_Space = numpy.linspace(0, 30, 100)

t_r = 1
zeta = 0.5
w_n = 1-0.4167*zeta+2.917*pow(zeta, 2)
K_approximation = 19.865497
a_approximation = pow(w_n, 2)/30
num1 = K_approximation
den1 = numpy.array([1, a_approximation + 30, 30 * a_approximation, K_approximation])
Ts1 = tf(num1, den1)
ys1, ts1 = step(Ts1, t_Space)
print(stepinfo(Ts1, t_Space))
print(K_approximation)
print(a_approximation)

k = 19.865497
a_list = numpy.linspace(0, 10, 10)

numpy.set_printoptions(precision=1)
pyplot.figure(dpi=100)
pyplot.plot(ts1, ys1, label=rf'K={K_approximation:3.1f}\nA={a_approximation:3.1f}')
for a in a_list :
    num2 = K_approximation
    den2 = numpy.array([1, a + 30, 30 * a, K_approximation])
    Ts2 = tf(num2, den2)
    ys2, ts2 = step(Ts2, t_Space)
    #print(stepinfo(Ts2, t_Space))
    pyplot.plot(ts2, ys2, label=rf'a={a:3.1f}')
pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
pyplot.show()
