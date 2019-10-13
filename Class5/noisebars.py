import random, time

def draw_to_screen(content):
    print("\n"*50)
    print(content)
    time.sleep(0.2)

def noise_bars(n, w):
    result = ""
    list_of_numbers = []
    for i in range(n):
        list_of_numbers.append(random.randint(1,w))

    while len(list_of_numbers) > 0:
        next_number = list_of_numbers.pop()
        result += "*"*next_number + "\n"
    return result

for i in range(60):
    draw_to_screen(noise_bars(18, 40))