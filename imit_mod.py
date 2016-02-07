import random
import matplotlib.pyplot as plt


P0 = float(raw_input("Input P0"))
P1 = float(raw_input("Input P1"))
A = float(raw_input("Input A"))
B = float(raw_input("Input B"))
K = float(raw_input("Input K"))
L = float(raw_input("Input L"))

D0 = A - (B*P0)
S0 = K + (L*P1)

Ustart = D0 *(-0.08)
Uend = D0 *(0.08)

if Ustart > Uend:
   Uend, Ustart = Ustart, Uend

Vstart = S0*(-0.02)
Vend = S0*(0.02)

if Vstart > Vend:
   Vend, Vstart = Vstart, Vend

Wstart = (S0-D0)*(-0.05)
Wend = (S0-D0)*(0.05)

if Wstart > Wend:
   Wend, Wstart = Wstart, Wend

Us = []
Vs = []
Ws = []

Pt = []

a = 0

while a<25:
   Us.append(random.uniform(Ustart, Uend))
   Vs.append(random.uniform(Vstart, Vend))
   Ws.append(random.uniform(Wstart, Wend))
   a = a + 1

for xa in Us:
   for xb in Ws:
      for xc in Vs:
         P = (A-K-L*P1+xa+xb-xc)/B
         Pt.append(P)



'''while a<len(Pt):
   print "Pt = " + str(a+1) + " " + str(Pt[a])
   a = a + 1'''

plt.plot(Pt)
plt.savefig('example.png')
plt.show()
