VCC = 20
VBE = 0.6356
VBC = 0.6127
Beta = 220.26684
R1 = 39*pow(10, 3)
R2 = 9.1*pow(10, 3)
RC = 3.9*pow(10, 3)
RE = 2.2*pow(10, 3)

R12_ratio = R2/(R1+R2)
Req = 1/((1/R1)+(1/R2))

IB = (VCC * R12_ratio - VBE) / (Req + Beta * RE)
print(IB)
IB_old = 0
while abs(IB-IB_old) > pow(10, -8):
    IB_old = IB
    VB = (VCC * R12_ratio) - (IB * Req)
    VE = VB - VBE
    IE = VE / RE
    IB = IE / (Beta + 1)


VB = (VCC * R12_ratio) - (IB * Req)
VE = VB - VBE
IE = VE / RE
IB = IE / (Beta + 1)

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



