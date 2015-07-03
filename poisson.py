import math, random, time

r = random.random

# ( L^k / k! ) * e^-L

# FOR ANOTHER TIME: GET THE CUMULATIVE TABLE BEFORE

def poisson0(l): # by Finnbar!
        C = math.exp(-l) # our constant term
        # Generate a cumulative frequency thingy
        Cumu = [0]
        k = 0
        Number = r()
        previous = 0
        while True:
                k += 1
                new = Cumu[-1] + (((l**k)*C)/math.factorial(k))
                if new == previous: # if stupidly small
                        Cumu.append(1)
                        break
                else:
                        Cumu.append(new)
                        previous = new
        k = 0
        while True:
                k += 1
                if Number < Cumu[k]:
                        return k

def poisson1(l): # by that Knuth bloke
        L = math.exp(-l)
        k = 0 # Number of chances when a particle has been emitted
        p = 1 # Is it greater than e^-l?
        while True:
                k += 1
                p *= r()
                if p <= L:
                        return k - 1

YOUR_FAVOURITE_POISSON_ALGORITHM = poisson0

def Geigerer(l,t):
        result = [0] * t
        for i in range(t):
                result[i] = YOUR_FAVOURITE_POISSON_ALGORITHM(l)
        for i in range(t):
                time.sleep(result[i]/10.0)
                print "BEEP! after "+str(result[i]/10.0)+" seconds."
        print "BEEEEEEEEP"

Geigerer(4,100)
