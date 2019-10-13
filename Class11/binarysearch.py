import random

L = [random.randint(0, 100000) for i in range(1000)]
L.sort()

def find_in_sorted(L, target):
    if len(L) == 1:
        #down to one, either it matches or it doesn't
        return L[0] == target
    elif len(L) == 0:
        #can't be in a length 0 list
        return False
    else:
        middle_index = len(L)//2
        print(middle_index, L[middle_index])
        if L[middle_index] == target:
            #got lucky and found it
            return True
        elif L[middle_index] < target:
            #check right side here
            return find_in_sorted(L[middle_index+1:], target)
            
        else:
            #check left side here
            return find_in_sorted(L[:middle_index], target)

print(find_in_sorted(L, L[random.randint(0,len(L)-1)]))