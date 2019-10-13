def is_prime(n):
    if n > 1 :
        for m in range (2,int((n**0.5)) + 1):
            if (n % m == 0) :
                return False
    else :
        return True
    return True    
    
print(is_prime(1))                