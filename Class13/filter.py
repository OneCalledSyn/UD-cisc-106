print([i**2 for i in range(10) if i % 2 == 1])

generator = (i**2 for i in range(10) if i % 2 == 1)

for x in generator:
    print(x)