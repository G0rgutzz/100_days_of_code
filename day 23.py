import time
import turtle


# screen parameters
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Gra w ketchup z samochodami')
screen.tracer(0)
# player
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()






# scoreboard
FONT = ("Courier", 24, "normal")
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()


# cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()


# key bindings
screen.listen()
screen.onkey(player.up, 'Up')
screen.onkey(player.down, 'Down')
screen.onkey(player.left, 'Left')
screen.onkey(player.right, 'Right')
# game
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
