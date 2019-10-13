import random

L = [random.randint(0, 10) for i in range(100)]

num_bigger_than_8 = len(list(filter(lambda x: x > 8, L)))

print("Out of 100 there were",num_bigger_than_8, "bigger than 8")