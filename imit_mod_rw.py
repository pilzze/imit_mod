import random
import matplotlib.pyplot as plt


P0 = float(raw_input("Input P0"))
P1 = float(raw_input("Input P1"))
A = float(raw_input("Input A"))
B = float(raw_input("Input B"))
K = float(raw_input("Input K"))
L = float(raw_input("Input L"))
x = str(raw_input("filename"))
Pt = [P0, P1]
for t in range(1, 250):
   D0s = []
   S0s = []
   S1s = []
   
   D0 = A - (B*P0)
   S0 = K + (L*P1)
   S1 = D0

   D0s.append(D0)
   S0s.append(S0)
   S1s.append(S1)
   
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

   P = (A-K-L*Pt[t-1]+random.uniform(Ustart, Uend)+random.uniform(Vstart, Vend)-random.uniform(Wstart, Wend))/B
   Pt.append(P)
   D0 = A - (B*Pt[t-1]) + random.uniform(Ustart, Uend)
   S0 = K + (L*Pt[t]) + random.uniform(Vstart, Vend)
   S1 = D0 + random.uniform(Wstart, Wend)
   

   '''print "D0 " + str(D0)
   print "S0 " + str(S0)
   print "Ustart " + str(Ustart)
   print "Uend " + str(Uend)
   print "Vstart " + str(Vstart)
   print "Vend " + str(Vend)
   print "Ustart " + str(Ustart)
   print "Wend " + str(Wend)'''
   Us = []
   Vs = []
   Ws = []

   '''while a<25:
      Us.append(random.uniform(Ustart, Uend))
      Vs.append(random.uniform(Vstart, Vend))
      Ws.append(random.uniform(Wstart, Wend))
      a = a + 1

   a = 0'''
      
   '''while a<25:'''
   
   print "iter " + str(t+1)
   print "P= " + str(P)
   print "D0= " + str(A - (B*P0) + random.uniform(Ustart, Uend))
   print "P= " + str(P)

   '''while a<len(Pt):
      print "Pt = " + str(a+1) + " " + str(Pt[a])
      a = a + 1'''

plt.plot(Pt)
plt.savefig('example'+x+'.png')
plt.show()

'''for xa in Us:
   for xb in Vs:
      for xc in Ws:
         P = (A-K-L*P1+xa+xb-xc)/B
         Pt.append(P)

plt.plot(Pt)
plt.savefig('example_many.png')
plt.show()'''
