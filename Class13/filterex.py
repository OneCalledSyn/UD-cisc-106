def is_single(person):
    return person["rel_stat"].lower() == "single"

people = [{"name":"Andy", "rel_stat":"married"}, {"name":"Sara", "rel_stat":"married"}, {"name":"Simone", "rel_stat":"single"}]

print(list(filter(is_single, people)))
#Consumes a Boolean function and an iterable, returns iterable for elements which the function returns True