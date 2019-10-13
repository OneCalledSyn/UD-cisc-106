def mygen(iterable):
    for x in iterable:
        yield 3*x + 1

someList = [9, 7, 5]

#These two both create generators that do the same things
agen = mygen(someList)
samegen = (3*x + 1 for x in someList)

#Double checking
for x in agen:
    print(x)
    if next(samegen) != x:
        print("uhoh")

#These two both create a list from the "generator"
tripList = list(mygen(someList))
sameList = [3*x + 1 for x in someList]

print("Same lists" if tripList == sameList else "Not same")