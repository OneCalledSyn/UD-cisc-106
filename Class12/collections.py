threes = {0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
twos = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
fives = {0, 5, 10, 15, 20, 25, 30}
universe = set(range(31))

print(threes.union(twos))
print(threes.intersection(twos))
print(threes.difference(twos))

modulo6 = threes.intersection(fives)

venn = modulo6.intersection(twos)

print(venn)