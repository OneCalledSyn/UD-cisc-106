L = [5,3,2,1,1,0]

def listsummer (L):
    if L == []:
        return 0
    else:
        return L[0] + listsummer(L[1:]) 
print(listsummer(L))        