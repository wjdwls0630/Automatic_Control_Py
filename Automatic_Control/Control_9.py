import numpy
from control.matlab import *

omega = 1
zeta = 0.7
num = numpy.array([1, 0, omega**2])
den = numpy.array([1, 2*zeta*omega, omega**2])
Gs = tf(num, den)

print(f'poles at {pole(Gs)}')
print(f'zeros at {zero(Gs)}')

# control.matlab.pzmap(Gs, Plot=True, grid=True, title="Pole Zero Map")
pzmap(Gs)

