L = [5,3,2,1,1,0]

def reverse(L):
    if L == []:
        return L
    else:
        return reverse(L[1:]) + [L[0]]
        
revL = reverse(L)

print(revL)