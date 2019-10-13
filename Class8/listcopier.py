import copy

def doSomeWork(person):
    print("{0} is doing 10 hours of work.".format(person["name"]))
    person["ProductionThisWeek"] += 100
    person["ProductiveHoursThisWeek"] -= 10
    
Andy = {"name": "Andy Novocin", "ProductiveHoursThisWeek": 70, "ProductionThisWeek": 0}

myClone = copy.copy(Andy)
myAlphaClone = copy.copy(Andy)
myBetaClone = copy.copy(Andy)
myGammaClone = copy.copy(Andy)

for i in range(1,8):
    doSomeWork(myClone)
    
for i in range(1,8):
    doSomeWork(myAlphaClone)
    
for i in range(1,8):
    doSomeWork(myBetaClone)
    
for i in range(1,8):
    doSomeWork(myGammaClone)    

print(myClone)
print(myAlphaClone)
print(myBetaClone)
print(myGammaClone)
print(Andy)