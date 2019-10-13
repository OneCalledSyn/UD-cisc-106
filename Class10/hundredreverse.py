def hundredreverse (n):
    if n > 1:
        print (n)
        return hundredreverse(n-3)
    else:
        return 1
        
print(hundredreverse(100))        