VCC = 10
VEE = -10
R1 = 1.2 * pow(10, 3)
R2 = 1.2 * pow(10, 3)
RL = 5.1 * pow(10, 3)
RE = 4.7 * pow(10, 3)

VBE = 0.6450
VBC = 0.6312

Beta = 128.672

VB = VEE*(R1/(R1+R2))
VE = VB-VBE
IE = (VE-VEE)/RE
IB = IE/(Beta+1)
IB_old = 0
while abs(IB-IB_old) > pow(10, -8):
    IB_old = IB
    VB = (1/((1/R1)+(1/R2)))*(VEE/R2-IB)
    VE = VB-VBE
    IE = (VE-VEE)/RE
    IB = IE / (Beta + 1)

VB = (1 / ((1 / R1) + (1 / R2))) * (VEE / R2 - IB)
VE = VB - VBE
IE = (VE - VEE) / RE
IB = IE / (Beta + 1)
IC = IB*Beta
VC = VCC - IC*RL

print(IB)
print(IC)
print(IE)
print(VB)
print(VC)
print(VE)
print(VB-VE)
print(VC-VE)







