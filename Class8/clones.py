Andy = {"name" : "Andy Novocin", "ProductiveHoursThisWeek" : 70, "ProductionThisWeek": 0}

def doSomeWork(person):
    print("{0} is doing 10 hours of work".format(person["name"]))
    person["ProductionThisWeek"] += 100
    person["ProductiveHoursThisWeek"] -= 10

ProfNovocin = Andy

print("Hours Available For Work: {0}".format(ProfNovocin["ProductiveHoursThisWeek"]))

doSomeWork(Andy)

print("Hours Available For Work: {0}".format(ProfNovocin["ProductiveHoursThisWeek"]))

#My alias didn't add any productive hours to my work week... I need a clone!
#This is "Hand-Cloning"
ClonedAndy = {}
for key in Andy:
    ClonedAndy[key] = Andy[key]

print("The next Andy to do work is my clone! Muah ha ha")
doSomeWork(ClonedAndy)

print("Hours Available For Work: {0}".format(ProfNovocin["ProductiveHoursThisWeek"]))

print("Hooray my clone did work, but Andy didn't drain any hours!")