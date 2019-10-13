jags = {"name": "The Jaguars", "score": 0}
colts = {"name": "The Colts", "score": 0}

def touchdown(some_team):
    #Add 7 points to a score here
    some_team["score"] += 7

def field_goal(some_team):
    #Add 3 points to a score here
    some_team["score"] += 3
    
field_goal(colts)
field_goal(jags)
touchdown(jags)
touchdown(colts)
#Halftime
#Nothing in 3rd quarter
field_goal(colts)
#missed twice
#field_goal(jags)
#field_goal(jags)
#Overtime
#missed again
#field_goal(jags)
field_goal(colts)
print("The final score is {0} to {1}. {2} are victorious!".format(
    jags["score"],
    colts["score"],
    jags["name"] if jags["score"] > colts["score"] else colts["name"]
    ))