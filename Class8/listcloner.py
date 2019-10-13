first_four = [1,2,3,4]

Clonedfirst_four = [0]*4
for i in range (0,4):
    Clonedfirst_four[i] = first_four[i]
    print(Clonedfirst_four[i])

Clonedfirst_four.append(5)
print(first_four)
print(Clonedfirst_four)