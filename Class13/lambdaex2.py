people = [{"name":"Andy", "rel_stat":"married"}, {"name":"Sara", "rel_stat":"married"}, {"name":"Simone", "rel_stat":"single"}]

print("Count married people")
print(list(map(lambda x: x["rel_stat"], people)))

print(list(map(lambda x: 1 if x["rel_stat"] == "married" else 0, people)))

print(sum(map(lambda x: 1 if x["rel_stat"] == "married" else 0, people)))


print("Evaluate a polynomial at many points:")
for i in map(lambda x: x**3 + 2*x -1, range(11)):
    print(i)