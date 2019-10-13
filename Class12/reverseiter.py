iterable_here = "Andy Rulz"

for variable_here in iterable_here:
    print(variable_here) #actions here

print("Is shorthand for:")

it = reversed(iterable_here)
while True:
    try:
        variable_here = next(it) #declare variable_here
    except StopIteration:
        break #break out of the loop if we're done
    print(variable_here) #actions here