import math
#Python first test RE:Poisson distribution.
#X is the number of happenings in a certain time period.
#Setting it at 5, can't be arsed to rig up an input right now.
X = 5
#Let's start with 5 in 10 seconds. uT is the starting time period.
#All variable names can and will change in the future.
uT = 10
T = uT*100
#Makes it easier to change in the future. T will be changing later on, and I'm still debating whether or not to do multiple tests.
#This is all written live, and comments will not be changed - think of it like a... train of consciousness? stream of consciousness?
#Fuck it I don't care what it's called. Point is, I'll be writing everything down as I think it.
#Gonna be using a for loop to print the probabilites from 0 up to... 100 for now.
#This can be hijacked later on for an actual simulation, but this is simple for now.
Xp = 0
#Xp will be in the for loop. Long story.
#Stands for "Probability of X".
Xprob = X/float(T)
#FUCKING FLOATS
#So, 5 over 10,000. Once again, quality of life.
#The lower piece of code is gonna go through like 10 iterations, so I will add comments below with mention of when they were done.
#Eurgh I hate factorials
print "Prefor"
FactorialT = math.factorial(T)
#Funfact, too large a T makes python crash. Totally didn''t take 10 mins to figure this out.
for Xp in range (0,100):
    print "Test"
    nCr = FactorialT/(math.factorial(Xp)*math.factorial(T-Xp))
    PofX = (Xprob**Xp)*((1-Xprob)**(T-Xp))*nCr
    print nCr
    print PofX
#IT WORKS! Okay, the above code is now obsolete.
#Please go to PoissonV2ForLoop.py if you want to see the working, clean, version.
    
    
