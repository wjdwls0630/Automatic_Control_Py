import numpy
from matplotlib import pyplot
from control.matlab import *

K = 10
a_list = numpy.linspace(0, 10, 10)
t_Space = numpy.linspace(0, 10, 100)
T_list = []
yT_list = []
tT_list = []
index1_list = []
index2_list = []
Rise_Time_list = []
for a in a_list:
    num = K
    den = numpy.array([1, a + 30, 30 * a, K])
    Ts = tf(num, den)
    T_list.append(Ts)
    ys, ts = step(Ts, t_Space)
    print(stepinfo(Ts, t_Space))

    yT_list.append(ys)
    tT_list.append(ts)








numpy.set_printoptions(precision=1)
pyplot.figure(dpi=100)
for i in range(0, len(T_list)):
    pyplot.plot(tT_list[i], yT_list[i], label=rf'$\zeta$={a_list[i]:3.1f}')


pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
pyplot.show()
