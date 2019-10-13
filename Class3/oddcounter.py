def oddcounter(n): 
    total = 0
    for i in range (1,n):
        if (i%2 == 0) :
            total = total
        else:
            total = total + i
    print("The sum of the odd integers less than " + str(n) + " is: " + str(total))
    
oddcounter(8);    
