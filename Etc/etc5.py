VCC = 10
RB1 = 6.8 * pow(10, 3)
RB2 = 5.6 * pow(10, 3)
RB3 = 4.7 * pow(10, 3)
RC = 1.8 * pow(10, 3)
RE = 1 * pow(10, 3)

VBE = 0.6504
VBC = 0.6221

Beta1 = 357.78
Beta2 = 152.8195764

VB1 = RB3/(RB1+RB2+RB3)*VCC
VB2 = (RB2+RB3)/(RB1+RB2+RB3)*VCC
VE1 = VB1 - VBE
IE1 = VE1/RE
IB1 = IE1/(Beta1)

IB_old = 0
while abs(IB1-IB_old) > pow(10, -8):
    IB_old = IB1
    VB1 = (1/((1/RB2)+(1/RB3)))*(VB2/RB2-IB1)
    VE1 = VB1-VBE
    IE1 = VE1/RE
    IB1 = IE1 / (Beta1 + 1)


VB1 = (1/((1/RB2)+(1/RB3)))*(VB2/RB2-IB1)
VE1 = VB1-VBE
IE1 = VE1/RE
IB1 = IE1 / (Beta1 + 1)
IC1 = Beta1*IB1

IE2 = IC1
IB2 = IE2/(Beta2+1)
VB2 = (1/((1/RB1)+(1/RB2)))*(VCC/RB1+VB1/RB2-IB2)
VE2 = VC1 = VB2 - VBE
IC2 = Beta2*IB2
VC2 = VCC-IC2*RC
print(IB1)
print(IC1)
print(IE1)
print(VB1)
print(VC1)
print(VE1)
print(VB1-VE1)
print(VC1-VE1)
print(IB2)
print(IC2)
print(IE2)
print(VB2)
print(VC2)
print(VE2)
print(VB2-VE2)
print(VC1-VE1)
print(VC2-VE2)




