numBin = input("Enter a base 10 number: ")

print ("Converted to binary: " + "{0:b}".format(numBin))

def show_first_n_binary_numbers(n):
    i = 0;
    while (i < n):
        print("{0} in binary: {0:b}".format(i))
        i = i + 1

show_first_n_binary_numbers(numBin)