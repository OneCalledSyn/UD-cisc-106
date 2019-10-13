def capitals (iterable) :
    for x in iterable :
        if x.isupper() == True :
            yield (x)

inspire = "I Am Good Enough, Smart Enough, and Doggone It People Like Me!"

my_gen = capitals(inspire)

for x in my_gen :
    print (x)
