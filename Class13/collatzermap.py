def collatzer(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n//2
    else:
        return 3*n + 1

#Use the output of map as an iterable
for i in map(collatzer, range(1, 11)):
    print(i)

#Or save it and map several times
r = range(1, 11)
for k in range(5):
    r = map(collatzer, r)
print(list(r))

#Or build a list out of it
print([i for i in map(collatzer, range(1, 11))])