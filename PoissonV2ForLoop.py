import math
X = 5
uT = 10
T = uT*100
Xp = 0
Xprob = X/float(T)
FactorialT = math.factorial(T)
for Xp in range (0,100):
    nCr = FactorialT/(math.factorial(Xp)*math.factorial(T-Xp))
    PofX = (Xprob**Xp)*((1-Xprob)**(T-Xp))*nCr
    print "P( X =", Xp, ") =", PofX
