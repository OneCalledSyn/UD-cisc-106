print("List of multiples of 5 less than 131: ")

print(list(filter(lambda x: x % 5 == 0, range(1,132))))