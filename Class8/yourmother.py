#YourMother = { "name": "Yo Mamma", "child": {"name": "Your Name Here", "age": "Twenty Something"} }

#import copy

#MommaClone = copy.copy(YourMother)

#MommaClone["child"]["name"] = "Your momma's clone's baby's name here"

#print(YourMother["child"]["name"]) #uhoh you lost your name

#print(dir(copy))

YourMother = { "name": "Yo Mamma", "child": {"name": "Your Name Here", "age": "Twenty Something"} }

import copy

MommaClone = copy.deepcopy(YourMother)

MommaClone["child"]["name"] = "Your momma's clone's baby's name here"

print(YourMother["child"]["name"]) #uhoh you lost your name


