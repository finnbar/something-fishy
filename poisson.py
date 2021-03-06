import math, random, time, urllib2

r = random.random

# ( L^k / k! ) * e^-L

'''
What does this do?
> It grabs a truly random seed from random.com
> It return Poisson-distributed random numbers
> It returns proper Poisson-distributed intervals
> These results have a mean and variance of roughly LAMBDA
> It has a very low score on the goodness of fit test (chi-squared)
> It will find cake for you*

* only on April 31st

'''

def newRandomSeed():
        # thanks random.org
        random.seed(urllib2.Request("https://www.random.org/integers/?num=1&min=0&max=1000000000&col=1&base=10&format=plain&rnd=new"))

def poisson0(l,Cumu=[],debug=False): # by Finnbar!
        if Cumu == []:
                Cumu = poissonCumulative(l,debug)
        Number = r() # r = random.random
        k = 0
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

YOUR_FAVOURITE_POISSON_ALGORITHM = poisson0
YOUR_FAVOURITE_RESULTS_SET = resultsSet2
THESE_VARIABLE_NAMES_ARE_FROM_A_COMP1_PAPER = True

def Geigerer(LAMBDA,tim):
        T = 0
        while T < tim:
                i = -math.log(1.0-r())/LAMBDA
                T += i
                print "BEEP after "+str(i)+" seconds."
                time.sleep(i)
        print "BEEEEEEEP"

def experimentalProbability(tab,n):
        return tab.count(n)/float(len(tab))

def goodnessOfFit(l,t,n):
        # Chi-squared test!
        tab = YOUR_FAVOURITE_RESULTS_SET(l, t)
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

def ask(): # this is not useful. In fact, it will probably form the base
           # for an elaborate joke in the presentation, or something.
        raw_input("What is your question? ")
        return "Yes"
