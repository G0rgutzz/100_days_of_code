import turtle
import time

# pong game
# screen parameters
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Gra w paletke z guwniarom')
screen.tracer(0)
SPEED = 10

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

# ball class
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.goto(0, 0)
        self.bouncey = 0
        self.bouncex = 0

    def move(self):
        new_x = self.xcor() + SPEED*((-1)**self.bouncex)
        new_y = self.ycor() + SPEED*((-1)**self.bouncey)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.bouncey += 1

    def bounce_x(self):
        self.bouncex += 1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_score()

    def lpoint(self):
        self.lscore += 1
        self.clear()
        self.update_score()

    def rpoint(self):
        self.rscore += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.goto(-100, 260)
        self.write(self.lscore, align="center", font=('Times New Roman', 30, 'normal'))
        self.goto(100, 260)
        self.write(self.rscore, align="center", font=('Times New Roman', 30, 'normal'))

    def game_over(self):
        self.color('white')
        self.penup()
        self.goto(0,0)
        self.write('Game Over', align='center', font=('Times New Roman', 20, 'normal'))


# game settings
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
# key bindings
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
# option for 2 player on one computer

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# actual game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    # collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # collision with right paddle
    if ball.xcor() > 320 and abs(ball.ycor() - r_paddle.ycor()) < 50:
        if 340 < ball.xcor() < 360 and abs(ball.ycor() - r_paddle.ycor()) < 50:
            ball.bounce_y()
            SPEED += 1
        else:
            ball.bounce_x()
            SPEED += 1
    # collision with left paddle
    if ball.xcor() < -320 and abs(ball.ycor() - l_paddle.ycor()) < 50:
        if -340 > ball.xcor() > -360 and abs(ball.ycor() - l_paddle.ycor()) < 50:
            ball.bounce_y()
            SPEED += 1
        else:
            ball.bounce_x()
            SPEED += 1
    # ball missed the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.lpoint()
        SPEED = 10
    # ball missed the left paddle
    elif ball.xcor() < -380:
        ball.reset_position()
        score.rpoint()
        SPEED = 10


screen.exitonclick()
