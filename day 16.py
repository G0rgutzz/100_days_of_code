import turtle
import prettytable
# few examples how classes and functions work
"""
timmy = turtle.Turtle()  # turtle
print(timmy)
timmy.shape('turtle')
timmy.color('cyan3')
timmy.forward(25)
timmy.left(90)
timmy.forward(100)
my_screen = turtle.Screen()  # showing it on the screen
print(my_screen.canvheight)
my_screen.exitonclick()  # screen that is closed by clicking on it
"""
# creating object from prettytable
table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.valign = 'b'
table.align = 'r'
print(table)
'''
class CarBlueprint():
    def move():
        speed = 60
    
    def stop():
        speed = 0
    
    speed = 0
    fuel = 32
    


car = CarBlueprint()
'''