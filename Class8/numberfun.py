x=5
y=x #Assign x to y
y=7 #redefine y
print(x)

x=[5]
y=x #Assign x to y
y[0]= 7 #Mutate a value in y
print(x)

x=[5]
y=x #Assign x to y
y=[7] #redefine y
print(x)