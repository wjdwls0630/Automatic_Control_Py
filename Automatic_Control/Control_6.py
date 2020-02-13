import numpy
from control.matlab import *

# 1/s+1
num1 = numpy.array([1])
den1 = numpy.array([1, 1])
G_1 = tf(num1, den1)

# 2/s+2
num2 = numpy.array([2])
den2 = numpy.array([1, 2])
G_2 = tf(num2, den2)

print(f'G_1={G_1}')
print(f'G_2={G_2}')
print(f'G_1+G_2={G_1+G_2}')
print(f'G_1 G_2={G_1*G_2}')