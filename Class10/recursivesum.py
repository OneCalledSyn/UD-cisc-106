total = 0

def hundredforward (n):
    if n < 100:
        global total
        total = total + n
        return hundredforward(n+3)
    else:
        return total
        
print(hundredforward(1))        