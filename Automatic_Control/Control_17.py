import numpy
from matplotlib import pyplot
from control.matlab import *

t_Space = numpy.linspace(0, 0.5, 100)

a_list = [5.50, 500]
T_list = []
ys_list = []
ts_list = []
# unity feedback
H = 1
den = numpy.array([1, 0, -1, 0])
for a in a_list:
    num = numpy.array([100, 100*(a + 2), 100*2 * a])
    G = tf(num, den)
    # negative
    T = feedback(G, H, -1)
    T_list.append(T)
    ys, ts = step(T, t_Space)
    print("maximum overshoot : {}".format(max(ys) - 1))
    ys_list.append(ys)
    ts_list.append(ts)
    print(stepinfo(T, t_Space))


numpy.set_printoptions(precision=1)
pyplot.figure(dpi=100)
for i in range(0, len(a_list)):
    pyplot.plot(ts_list[i], ys_list[i], label=rf'a={a_list[i]:3.1f}')

pyplot.title('Step_Response that a changes')

pyplot.xlabel(r'$t$ (sec)')
pyplot.ylabel(r'$y$')
pyplot.legend()
pyplot.grid()
pyplot.savefig("Automatic_Control_7_41_c.png")
pyplot.show()