import numpy
from matplotlib import pyplot
from control.matlab import *


t_Space = numpy.linspace(0, 200, 1000)
N_list = [1, 10]
den1 = numpy.array([0.05, 0.55, 0.5, 0])
T_list = []
ys_list = []
ts_list = []
# original
for N in N_list:
    num = 0.5 * N
    G = tf(num, den1)
    T = feedback(G, 1, -1)
    T_list.append(T)
    ys, ts = step(T, t_Space)
    ys_list.append(ys)
    ts_list.append(ts)
    print("original N = {} : {}".format(N, stepinfo(T)))

# approximation
den2 = numpy.array([1, 1, 0])
for N in N_list:
    num = 0.5 * N
    G = tf(num, den2)
    T = feedback(G, 1, -1)
    T_list.append(T)
    ys, ts = step(T, t_Space)
    ys_list.append(ys)
    ts_list.append(ts)
    print("approximation N = {} : {}".format(N, stepinfo(T)))

numpy.set_printoptions(precision=1)
pyplot.figure(dpi=100)
for i in range(0, 2):
    pyplot.plot(ts_list[i], ys_list[i], label=rf'Original : N={N_list[i]:3.1f}')

for i in range(2, 4):
    pyplot.plot(ts_list[i], ys_list[i], label=rf'Approximation : N={N_list[i-2]:3.1f}')
pyplot.title('Step_Response that N changes')

pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
pyplot.savefig("Automatic_Control_7_42_b.png")
pyplot.show()





