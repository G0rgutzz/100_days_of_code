import turtle
import random

timmy = turtle.Turtle()  # turtle
my_screen = turtle.Screen()  # showing it on the screen
print(timmy)
# timmy.shape('circle')
timmy.color('black')
timmy.speed(10)
timmy.width(2)
my_screen.colormode(255)

def straight_line(length, angle):
    timmy.right(angle)
    timmy.forward(length)

def polygon(length, amount):
    for j in range(0, amount):
        straight_line(length, 180-((amount-2)*180)/amount)

def dashed_line(length):
    for k in range(0, 10):
        timmy.pendown()
        timmy.forward(length)
        timmy.pu()
        timmy.forward(length)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb
def random_move(moves):
    direction = (0, 90, 180, 270)
    for l in range(0, moves):
        timmy.color(random_color())
        timmy.right(random.choice(direction))
        timmy.forward(20)

def series_of_circles(amount):
    for n in range(0, amount):
        timmy.circle(radius=100)
        timmy.color(random_color())
        timmy.left(360/amount)

def spirograph(number_of_spirals, number_of_circles, gap):
    for m in range(0, number_of_spirals):
        series_of_circles(number_of_circles)
        timmy.forward(gap)

"""
# dashed_line(10)
# creates polygons in a given range, each with different color
for i in range(3, 9):
    timmy.color(random_color())
    polygon(100, i)
"""
# random_move(20)
spirograph(5, 30, 20)
# series_of_circles(50)
my_screen.exitonclick()  # screen that is closed by clicking on it