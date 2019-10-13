S = 'chungus'

def revstr(S):
    if len(S) == 1 :
        return S
    else :
        return S[-1] + revstr(S[:-1])
print(revstr(S))        