VCC = 10
VEE = -10
VBE = 0.7
Beta3 = 225.2207477
RB = 20*pow(10, 3)
RC = 9.1*pow(10, 3)
RE = 4.3*pow(10, 3)
R1 = 9.1*pow(10, 3)
R2 = 9.1*pow(10, 3)

Req1 = 1/((1/R1)+(1/R2))
Req2 = 1/((1/R1)+(1/R2)+(1/((Beta3+1)*RE)))

VB3 = ((VEE+VBE)/((Beta3+1)*RE))+VEE/R2
VB3 *= Req2
IB3 = (VEE-VB3)/R2 - VB3/R1
VE3 = VB3 - VBE
IE3 = (VE3 - VEE) / RE

IC3 = IB3*Beta3

IE1 = IE2 = 0.5*IC3

Beta = 240.2062179
IB1 = IE1/(Beta+1)
VB1 = -IB1*RB
IC1 = Beta*IB1
VC1 = VCC - RC*IC1

print(VC1)




