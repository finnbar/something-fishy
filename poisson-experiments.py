import math, random

r = random.random

def exponentionalProbabilityDensity(l,x):
    if x>=0: return l*math.exp(-l*x)
    return 0

def exponentialContinuous(l,rang,t):
    prev = 0
    res = []
    for i in range(t):
        nex = prev + (float(rang)/float(t))
        res.append(math.exp(-l*prev) - math.exp(-l*nex))
        prev = nex
    return res

def exponentialPoisson(l,seconds,precision):
    results = []
    for i in range(seconds):
        events = 0
        for j in cont:
            if r() < j:
                events += 1
        results.append(events)
    return results
