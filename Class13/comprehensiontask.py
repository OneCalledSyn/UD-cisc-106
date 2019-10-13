def psquares (iterable) :
    for x in iterable :
        yield x**2

numList = [1,2,3,4,5,6,7,8,9,10]

my_gen = psquares(numList)

for x in my_gen :
    print(x)