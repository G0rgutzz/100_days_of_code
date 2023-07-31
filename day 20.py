import random
import turtle
import time

# snake game
# screen parameters
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Gra w wonsza')
screen.tracer(0)
# speed and starting positions of the snake
SPEED = 20
START_POS = [[0, 0], [-20, 0], [-40, 0]]
# class to create snake body and move it
class Snake:
    def __init__(self):
        self.segments = []
        self.snake_body()
        self.head = self.segments[0]

    def snake_body(self):
        for position in START_POS:
            self.grow(position)

    def move_forward(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(SPEED)

    def grow(self, position):
        body = turtle.Turtle(shape='square')
        body.color('white')
        body.penup()
        body.setposition(position)
        self.segments.append(body)

    def extend(self):
        self.grow(self.segments[-1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

# detecting collision with food
class Food(turtle.Turtle):
    # inheriting from turtle
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # gives size 10x10
        self.color('blue')
        self.speed(10)  # no animations
        self.new_location()

    def new_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# class for keeping a score
class Scoreboard(turtle.Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def new_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(arg=f'score: {self.score}', align='center',
                   font=('Times New Roman', 14, 'normal'))

    def game_over(self):
        self.color('white')
        self.penup()
        self.goto(0,0)
        self.write('Game Over', align='center', font=('Times New Roman', 20, 'normal'))


snake = Snake()
food = Food()
scoreboard = Scoreboard()
# code to control the snake
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.07)
    snake.move_forward()
    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.new_location()
        snake.extend()
        scoreboard.new_score()
# detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

# detecting collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
