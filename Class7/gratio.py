fiblist = [0,1]
for i in range(20):
    fiblist.append(fiblist[i] + fiblist[i+1])
print (fiblist)

golden=[fiblist[i] / float(fiblist[i-1]) for i in range(2,len(fiblist))]
print (golden)