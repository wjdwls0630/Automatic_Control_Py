VCC = 10
VEE = -10
VBE = 0.7
Beta = 230.4697894
RB = 20*pow(10, 3)
RC = 9.1*pow(10, 3)
RE = 9.1*pow(10, 3)


IB = (2*VEE+2*VBE)/(-2*RB-4*(Beta+1)*RE)
IB_old = 0
while abs(IB-IB_old) > pow(10, -8):
    IB_old = IB
    VB = -RB*IB
    VE = VB-VBE
    IE = (VE-VEE)/RE
    IB = IE / (2*(Beta + 1))

VB = -RB * IB
VE = VB - VBE
IE = (VE - VEE) / RE
IB = IE / (2 * (Beta + 1))
IC = Beta*IB
VC = VCC - RC*IC
print(IB)
print(IC)
print(IE)
print(VB)
print(VE)
print(VC)
print(VB-VE)
print(VC-VE)



