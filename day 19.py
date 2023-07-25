import random
import turtle

# turtle race
screen = turtle.Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win?")
print(bet)
turtles =[]
rainbow = ['purple', 'red', 'yellow', 'blue', 'green', 'black']
for turtle_index in range(0,6):
    timmy = turtle.Turtle(shape='turtle')
    timmy.color(rainbow[turtle_index])
    timmy.penup()
    timmy.setposition(x=-230, y=-100+turtle_index*30)
    turtles.append(timmy)

def move_forward():
    if bet:
        lights = True
    while lights:
        for turtle in turtles:
            if turtle.xcor() > 230:
                winner = turtle.pencolor()
                if winner == bet:
                    screen.textinput(title="You've won", prompt=f"The winner {winner} turtle")
                else:
                    screen.textinput(title="You've lost.", prompt=f"The winner {winner} turtle")
                lights = False
            else:
                turtle.forward(random.randint(0,10))


move_forward()
""" # functions to draw on the screen based on the keyboard input
def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def move_counterclockwise():
    timmy.setheading(timmy.heading()+5)

def move_clockwise():
    timmy.setheading(timmy.heading()-5)

def reset_turtle():
    screen.resetscreen()
    timmy.setposition(0, 0)


screen.listen()
screen.onkeypress(fun=move_forward, key='w')
screen.onkeypress(fun=move_backward, key='s')
screen.onkeypress(fun=move_counterclockwise, key='a')
screen.onkeypress(fun=move_clockwise, key='d')
screen.onkeypress(fun=reset_turtle, key='c')
"""



screen.exitonclick()
