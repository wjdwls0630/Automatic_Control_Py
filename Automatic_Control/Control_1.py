import numpy as np
from control.matlab import *


num1 = np.array([1])
den1 = np.array([1, 1])
G_1 = tf(num1, den1)
print(G_1)