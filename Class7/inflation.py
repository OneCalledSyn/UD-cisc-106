import math

inflation = .03

def endowment(rate, principal, col, prison_time) :
    return principal*math.exp(rate*prison_time)
    
print (endowment(.04, 10000, 0, 5))    