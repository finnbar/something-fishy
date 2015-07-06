import math, random, time, urllib2

r = random.random

# ( L^k / k! ) * e^-L

def newRandomSeed():
        # thanks random.com
        random.seed(urllib2.Request("https://www.random.org/integers/?num=1&min=0&max=1000000000&col=1&base=10&format=plain&rnd=new"))

def poisson0(l,Cumu=[],debug=False): # by Finnbar!
        Number = r()
        k = 0
        if Cumu == []:
                Cumu = poissonCumulative(l,debug)
        while True:
                if Number < Cumu[k]:
                        return k
                k += 1

def poissonCumulative(l,debug):
        # Generate a cumulative frequency thingy
        Cumu = [0]
        k = 0
        previous = 0
        while True:
                nextProb = getPoisson(l,k)
                new = Cumu[-1] + nextProb
                if new == previous: # if stupidly small difference
                        Cumu.append(1)
                        break
                else:
                        Cumu.append(new)
                        previous = new
                k += 1
        k = 0
        Cumu = Cumu[1:]
        if debug: print Cumu
        return Cumu

def poisson1(l,Cumu=[],debug=False): # by that Knuth bloke
        L = math.exp(-l)
        k = 0 # Number of chances when a particle has been emitted
        p = 1 # Is it greater than e^-l?
        while True:
                k += 1
                p *= r()
                if p <= L:
                        return k - 1

def poisson2(l,t): # thanks to http://preshing.com/20111007/how-to-generate-random-timings-for-a-poisson-process/
        Time = 0
        Timings = []
        while Time < t:
                Time += -math.log(1.0 - r()) / l
                if Time < t: # may have become > t since the while check
                        Timings.append(Time)
        return Timings

YOUR_FAVOURITE_POISSON_ALGORITHM = poisson0
THESE_VARIABLE_NAMES_ARE_FROM_A_COMP1_PAPER = True

def resultsSet(l,t):
        r = []
        c = poissonCumulative(l,False)
        for i in range(t):
              r.append(YOUR_FAVOURITE_POISSON_ALGORITHM(l,c))
        return r

def resultsSet2(l,t):
        r = []
        for i in range(t):
                r.append(len(poisson2(l,1)))
        return r

def experimentalProbability(tab,n):
        return tab.count(n)/float(len(tab))

def goodnessOfFit(l,t,n):
        # Chi-squared test!
        tab = resultsSet(l, t)
        x2 = 0
        for i in range(n):
                oi = float(experimentalProbability(tab,i))
                ei = float(getPoisson(l,i))
                if ei == 0:
                        break
                x2 += ((oi-ei)**2)/ei
        return x2

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

def getPoisson(l,k):
    return math.exp(-l) * ((l**k)/math.factorial(k)) 
