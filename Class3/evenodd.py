import random

def roll_die():
    return random.randint(1,6)

def is_even(n):
    if (n % 2 == 0):
        return True
    else:
        return False

print("Rolling a die 10 times")

for i in range(10):
    rolled_value = roll_die()
    message = "Even:" if is_even(rolled_value) else "Odd:"
    print(message, rolled_value, sep="\t")