iterable_here = "Andy Is The GreatEst"
s = [x.lower() for x in iterable_here if x.isupper()]
print("".join(s))

upper_bound = range (0, int(1000**(1/2)))
t = [x**2 for x in upper_bound if x % 2 == 1]
print(t)