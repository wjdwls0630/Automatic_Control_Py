import numpy
from matplotlib import pyplot
from control.matlab import *

t_Space = numpy.linspace(0, 20, 1000)

K = 69.582
a = 1.6021223
num = K
den = numpy.array([1, a + 30, 30 * a, K])
T1 = tf(num, den)
ys1, ts1 = step(T1, t_Space)

print(stepinfo(T1))

w_n = 1.5209
zeta = 0.5
num1 = K / 30.0812223
den1 = numpy.array([1, 2*zeta*w_n, pow(w_n, 2)])
T2 = tf(num1, den1)
ys2, ts2 = step(T2, t_Space)

print(stepinfo(T2))




numpy.set_printoptions(precision=1)
pyplot.figure(dpi=100)

pyplot.plot(ts1, ys1, label=rf'original K={K:3.1f}\na={a:3.1f}')
pyplot.plot(ts2, ys2, label=rf'approximation K={K:3.1f}\na={a:3.1f}')
pyplot.title('Step_Response : {}'.format(T1))

pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
# pyplot.savefig("Automatic_Control_7_28.png")
pyplot.show()