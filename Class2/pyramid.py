layers = input("How many layers should the pyramid be? ")
print ("This pyramid is " + layers + " layers high.")

p = 0

while p <= int(layers) :
    print (" " * (int(layers) - p + 1) + "* "*p)
    p += 1
    