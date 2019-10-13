def gcd(x,y):
    if y > x :
        return gcd(y,x)
    if x % y == 0 :
        return y
    return gcd(y, x % y)
    
print(gcd(8,4))    