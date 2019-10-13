counter = 0

def collatz(n):
    global counter
    
    if n == 1 :
        return counter
    elif (n % 2) == 0 :
        counter += 1
        return collatz(n/2)
    else:
        counter += 1
        return collatz(3*n + 1)
        
print(collatz(1000))    