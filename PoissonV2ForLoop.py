import math
import random

def ForPoisson(X,T,Time):
    Xp = 0
    T = T*1000
    Xprob = X/float(T)
    FactorialT = math.factorial(T)
    for Xp in range (0,Time+1):
        nCr = FactorialT/(math.factorial(Xp)*math.factorial(T-Xp))
        PofX = (Xprob**Xp)*((1-Xprob)**(T-Xp))*nCr
        print "P( X =", Xp, ") =", PofX

def ForPoissonSingle(Xp, X):
    #XP is the probability (X=0, X=1 ect) that you're generating.
    #X is the number of events in whatever time period you're specifying.
    T = 1000
    FactorialT = math.factorial(T)
    #T is a stupid big number.
    #FactorialT is a dumb thing for dumb people that I hate
    nCr = FactorialT/(math.factorial(Xp)*math.factorial(T-Xp))
    #nCr makes me angry
    Xprob = X/float(T)
    PofX = (Xprob**Xp)*((1-Xprob)**(T-Xp))*nCr
    return PofX

def PoissonRandomNumber(X):
    RN = random.random()
    RNGenned = False
    i = -1
    Prob = 0
    while RNGenned == False:
        i = i+1
        Prob = Prob + ForPoissonSingle(i, X)
        if Prob >= RN:
            RNGenned = True
    return i
        

def resultsSet(l,t):
        r = []
        for i in range(t):
              r.append(PoissonRandomNumber(l))
        return r

def findMean(tab):
        tot = 0
        div = 0
        for i in tab:
                tot += i
                div += 1.0
        return tot/div

def findVariance(tab):
        div = 0
        tot2 = 0
        for i in tab:
                tot2 += i**2
                div += 1
        return (tot2-(div*(findMean(tab)**2)))/div
