import math
import random

# THIS DOESN'T WORK
# THIS IS JUST HERE BECAUSE IT MIGHT BE USEFUL AT SOME POINT I GUESS...

def lockedPoisson(l,o):
    choices = []
    p = 1
    v = 0
    while p > 0:
        p = getPoisson(l,v)
        for i in range(int(round(p*o))):
            choices.append(v)
        v += 1
    while len(choices)<o:
        choices.append(l)
    random.shuffle(choices)
    return choices
    
def getPoisson(l,k):
    return math.exp(-l) * ((l**k)/math.factorial(k))

def findMean(tab):
    tot = 0
    div = 0
    for i in tab:
        tot += i
        div += 1.0
    return tot/div
