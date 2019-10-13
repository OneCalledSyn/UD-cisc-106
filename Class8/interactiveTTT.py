import turtle


boxsize = 50
tommy = turtle.Turtle()
tommy.speed(500)
screen = turtle.Screen()

def draw_circle(color, size, x, y, turtle=tommy):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def draw_line(x1, y1, x2=0, y2=0, turtle=tommy):
  turtle.penup()
  turtle.goto(x1,y1)
  turtle.pendown()
  turtle.goto(x2,y2)
  turtle.penup()


player_1_turn = True
penColor = "red"

circle_size = 40

the_game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def evaluate_game_state():
  winning_lines = [
    [[0,0], [0,1], [0,2]], 
    [[1,0], [1,1], [1,2]], 
    [[2,0], [2,1], [2,2]],
    [[0,0], [1,0], [2,0]], 
    [[0,1], [1,1], [2,1]], 
    [[0,2], [1,2], [2,2]], 
    [[0,0], [1,1], [2,2]], 
    [[0,2], [1,1], [2,0]]
  ]
  isFull = True
  for line in winning_lines:
    line_value = 0
    winner = 1
    count = 0
    for space in line:
      space_value = the_game[space[0]][space[1]]
      if space_value == 0:
        isFull = False
        break
      count += 1
      if line_value == 0:
        line_value = space_value
      else:
        if line_value != space_value:
          winner = 0
      if count == 3:
        if winner == 1:
          return line_value
  if isFull:
    return 0
  return 1

def convert_mouse_to_game(mouse_x, mouse_y):
  gx = -10
  if mouse_x < -50:
    gx = 0
  elif mouse_x < 50:
    gx = 1
  else:
    gx = 2
    
  gy = -10
  if mouse_y < -50:
    gy = 0
  elif mouse_y < 50:
    gy = 1
  else:
    gy = 2
  return gx, gy

def player_move(mouse_x, mouse_y):
  global player_1_turn, the_game, record
  
  from_game_to_xy = {
    0: -100,
    1: 0,
    2: 100
  }
  
  gx, gy = convert_mouse_to_game(mouse_x, mouse_y)
  if the_game[gx][gy] == 0:
    if player_1_turn:
      penColor = "red"
    else:
      penColor = "blue"
    the_game[gx][gy] = penColor
    player_1_turn = not player_1_turn
    draw_circle(penColor, circle_size, from_game_to_xy[gx], from_game_to_xy[gy] - (circle_size))
    result = evaluate_game_state()
    if result == 0:
      tommy.color("black")
      record[2] += 1
      start_game("Tie: {0}-{1}-{2}".format(record[0], record[1], record[2]))
    elif result == "red":
      record[0] += 1
      start_game("Red Wins: {0}-{1}-{2}".format(record[0], record[1], record[2]))
    elif result == "blue":
      record[1] += 1
      start_game("Blue Wins: {0}-{1}-{2}".format(record[0], record[1], record[2]))

def start_game(opening_text):
  global the_game, player_1_turn, penColor
  tommy.clear()
  tommy.penup()
  tommy.goto(-125, 175)
  tommy.write(opening_text, font=("Arial", 16, "normal"))
  tommy.color("black")
  draw_line(-boxsize, 3 * boxsize, -boxsize, -3 * boxsize, tommy)
  draw_line(boxsize, 3 * boxsize, boxsize, -3 * boxsize, tommy)
  draw_line( -3 * boxsize, boxsize, 3 * boxsize, boxsize, tommy)
  draw_line( -3 * boxsize, -boxsize, 3 * boxsize, -boxsize, tommy)
  the_game = [[0,0,0], [0,0,0], [0,0,0]]
  player_1_turn = True
  penColor = "red"

record = [0,0,0]
start_game("Welcome to TTT")
screen.onclick(player_move)