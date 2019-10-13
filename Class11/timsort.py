import random

L = [random.randint(0, 100000) for i in range(1000)]
L.sort()

print(L)
#Python sort method is Timsort, with O(n log n). Sorts from smallest to largest.