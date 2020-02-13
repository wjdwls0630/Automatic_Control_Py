from __future__ import division

import numpy
from matplotlib import pyplot
from control.matlab import *
from scipy.signal.ltisys import lti, bode, TransferFunction as TransFun


class ltimul(TransFun):
    def __neg__(self):
        return ltimul(-self.num,self.den)

    def __floordiv__(self,other):
        # can't make sense of integer division right now
        return NotImplemented

    def __mul__(self,other):
        if type(other) in [int, float]:
            return ltimul(self.num*other,self.den)
        elif type(other) in [TransFun, ltimul]:
            numer = numpy.polymul(self.num,other.num)
            denom = numpy.polymul(self.den,other.den)
            return ltimul(numer,denom)

    def __truediv__(self,other):
        if type(other) in [int, float]:
            return ltimul(self.num,self.den*other)
        if type(other) in [TransFun, ltimul]:
            numer = numpy.polymul(self.num,other.den)
            denom = numpy.polymul(self.den,other.num)
            return ltimul(numer,denom)

    def __rtruediv__(self,other):
        if type(other) in [int, float]:
            return ltimul(other*self.den,self.num)
        if type(other) in [TransFun, ltimul]:
            numer = numpy.polymul(self.den,other.num)
            denom = numpy.polymul(self.num,other.den)
            return ltimul(numer,denom)

    def __add__(self,other):
        if type(other) in [int, float]:
            return ltimul(numpy.polyadd(self.num,self.den*other),self.den)
        if type(other) in [TransFun, type(self)]:
            numer = numpy.polyadd(numpy.polymul(self.num,other.den),polymul(self.den,other.num))
            denom = numpy.polymul(self.den,other.den)
            return ltimul(numer,denom)

    def __sub__(self,other):
        if type(other) in [int, float]:
            return ltimul(numpy.polyadd(self.num,-self.den*other),self.den)
        if type(other) in [TransFun, type(self)]:
            numer = numpy.polyadd(numpy.polymul(self.num,other.den),-polymul(self.den,other.num))
            denom = numpy.polymul(self.den,other.den)
            return ltimul(numer,denom)

    def __rsub__(self,other):
        if type(other) in [int, float]:
            return ltimul(numpy.polyadd(-self.num,self.den*other),self.den)
        if type(other) in [TransFun, type(self)]:
            numer = numpy.polyadd(numpy.polymul(other.num,self.den),-polymul(other.den,self.num))
            denom = numpy.polymul(self.den,other.den)
            return ltimul(numer,denom)

    # sheer laziness: symmetric behaviour for commutative operators
    __rmul__ = __mul__
    __radd__ = __add__


# fcs high pass
fcs = 6.056798
num1 = numpy.array([1, 0])
den1 = numpy.array([1, 2*numpy.pi*fcs])
G1 = ltimul(num1, den1)

# fcc high pass
fcc = 29.69413
num2 = numpy.array([1, 0])
den2 = numpy.array([1, 2*numpy.pi*fcc])
G2 = ltimul(num2, den2)

# fce high pass
fce = 66.923241
num3 = numpy.array([1, 0])
den3 = numpy.array([1, 2*numpy.pi*fce])
G3 = ltimul(num3, den3)

#fhi low pass
fhi = 20.0556*pow(10, 6)
num4 = numpy.array([2*numpy.pi*fhi])
den4 = numpy.array([1, 2*numpy.pi*fhi])
G4 = ltimul(num4, den4)

#fho low pass
fho = 27.843813 *pow(10, 6)
num5 = numpy.array([2*numpy.pi*fho])
den5 = numpy.array([1, 2*numpy.pi*fho])
G5 = ltimul(num5, den5)

num6 = numpy.array([-70])
den6 = numpy.array([1])
Av_mid = ltimul(num6, den6)

G_temp = Av_mid*G1*G2*G3*G4*G5
G = lti(G_temp.num, G_temp.den)

print(G)

data_freq = numpy.array([50, 100, 200,	400, 600, 800,
     1*pow(10, 3), 2*pow(10, 3), 3*pow(10, 3), 5*pow(10, 3), 10*pow(10, 3),
     50*pow(10, 3), 100*pow(10, 3), 200*pow(10, 3), 500*pow(10, 3), 600*pow(10, 3),
     700*pow(10, 3), 800*pow(10, 3), 900*pow(10, 3), 1*pow(10, 6), 2*pow(10, 6)])

data_Av = numpy.array(
    [14, 28, 46, 58, 64, 65, 70, 70, 70, 70, 70,
     70, 70, 70, 70, 70, 70, 70, 70, 70, 70])

w, mag, phase = bode(G, numpy.logspace(1, 9).tolist())
f = w/(2*numpy.pi)
pyplot.figure(figsize=(15, 10))
pyplot.subplot(211)
pyplot.title("Ex25_4_a_Bode_Mag")
pyplot.semilogx(f, mag, lw=5, label="Formula")    # Bode magnitude plot
pyplot.plot(data_freq, 20*numpy.log10(data_Av), '.--', lw=5, label="Experiment_Data")
pyplot.ylim([-40, 40])
pyplot.ylabel('Magnitude (dB)')
pyplot.xlabel("Frequency (Hz)")
pyplot.legend()
pyplot.grid(True)

pyplot.subplot(212)
pyplot.title("Ex25_4_a_Bode_Phase")
pyplot.semilogx(w, phase, lw=5, label="Formula")  # Bode phase plot
pyplot.ylim([-360, 10])
pyplot.ylabel('Phase (deg)')
pyplot.xlabel("Frequency (Hz)")
pyplot.legend()
pyplot.grid(True)
pyplot.savefig("Ex25_4_a_Bode.png")
pyplot.show()

