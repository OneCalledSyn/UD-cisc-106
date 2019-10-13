#Select from four choices randomly, probably need to import random
#Map the four choices to the directions up, down, left, and right

import random

brownian = [(0,1), (1,0), (-1,0), (0,-1)]
grid_size = 10

x = input("Start from this x-coordinate: ")
y = input ("Start from this y-coordinate: ")

start_position = (x,y)

dx, dy = random.choice(brownian)

x =+ dx
y =+ dy

