def golden(x):
    if x == 0:
        return 1
    else:
        return(1 + (1 / golden(x-1)))
print(golden(20))
