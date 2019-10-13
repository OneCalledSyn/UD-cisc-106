import math

def year_interest(principle, rate):
    return principle*math.exp(rate)

print(year_interest(100000, .13))