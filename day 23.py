import time
import turtle
import random


# screen parameters
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Gra w ketchup z samochodami')
screen.tracer(0)
screen.colormode(255)
# player
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setheading(90)
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.setheading(270)
        self.goto(self.xcor(), new_y)

    def t_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.setheading(180)
        self.goto(new_x, self.ycor())

    def t_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.setheading(0)
        self.goto(new_x, self.ycor())



# scoreboard
FONT = ("Courier", 24, "normal")
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('Black')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def next_level(self):
        self.level += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.goto(-150, 260)
        self.write(f"Level: {self.level}", align="center", font=('Times New Roman', 25, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align='center', font=FONT)


# cars
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=2)
        self.setheading(90)
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.color(self.r, self.g, self.b)
        self.penup()
        self.goto(random.randint(-320, 320), random.randint(-250, 250))

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE - MOVE_DISTANCE*(score.level - 1)
        self.goto(new_x, self.ycor())
        self.car_reset()

    def car_reset(self):
        if self.xcor() < -320:
            self.goto(320, self.ycor())


# game settings
player = Player()
score = Scoreboard()
cars = []
for car in range(0,50):
    car = CarManager()
    cars.append(car)

# key bindings
screen.listen()
screen.onkey(player.up, 'Up')
screen.onkey(player.down, 'Down')
screen.onkey(player.t_left, 'Left')
screen.onkey(player.t_right, 'Right')
# game
game_on = True
while game_on:
    for car in cars:
        car.move()
        if car.distance(player) < 20:
            score.game_over()
            game_on = False
    time.sleep(0.1)
    screen.update()
    if player.ycor() > FINISH_LINE_Y:
        score.next_level()
        player.goto(STARTING_POSITION)


screen.exitonclick()
