def grim():
    r = range(100,0,-3)
    L = list(r)
    L[5:33:3] = range(10)
    print (L)
    
grim()