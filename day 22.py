import turtle
import time

# pong game
# screen parameters
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Gra w paletke z guwniarom')
screen.tracer(0)

# paddle class
class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

# game settings
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# key bindings
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
# option for 2 player on one computer
"""
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
"""
# actual game
game_on = True
while game_on:
    screen.update()
    #time.sleep(0.01)

screen.exitonclick()
