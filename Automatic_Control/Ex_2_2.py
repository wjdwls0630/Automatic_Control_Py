import numpy
from matplotlib import pyplot
from copy import deepcopy

V_D = numpy.array([0, 0.48374, 0.51947, 0.53932, 0.55324, 0.56537, 0.57452, 0.58168, 0.58872, 0.59488, 0.59991, 0.63670, 0.65641, 0.67041, 0.68141, 0.69054, 0.69819, 0.70548, 0.71130, 0.71661])
V_R = numpy.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10])
R_meas = 0.99716

I_D = V_R/R_meas

x_approx = numpy.arange(0, 0.71, 0.01)
slope = (I_D[15]-I_D[14])/(V_D[15]-V_D[14])
y_approx = slope*(x_approx-V_D[14])+I_D[14]

V_T = -I_D[14]/slope+V_D[14]
print(V_T)

numpy.set_printoptions(precision=7)
pyplot.figure(dpi=100)
pyplot.figure(figsize=(8, 6))
pyplot.title("Experiment_2_I-V_Curve")
pyplot.plot(V_D, I_D, label=r"$i-v$")

#pyplot.plot(x_approx, y_approx, label=r"$approx" )
pyplot.ylim([0,10])


"""
user_interval = 0.01

for _x in numpy.arange(min(V_D), max(V_D), user_interval):
    pyplot.axvline(x=_x, ls='-', color='#999999')

for _y in numpy.arange(min(I_D), max(I_D), user_interval):
    pyplot.axhline(y=_y, ls='-', color='#999999')
    
"""
pyplot.xlabel(r"$V_D(V)$")
pyplot.ylabel(r"$I_D(mA)$")
pyplot.grid(b=True, which='major', color='#666666', linestyle='-')
pyplot.minorticks_on()
pyplot.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.1)
pyplot.legend()
pyplot.savefig("Ex_2_e_1.png")
pyplot.show()



