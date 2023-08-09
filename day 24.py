
# reading a file and closing it after indentation ends
# mode is set as read only by default

with open('Input/Names/invited_names.txt') as file:
    a = file.read()
    names = a.split('\n')

with open('Input/Letters/starting_letter.txt', mode='r') as letter:
    b = letter.read()
    for i in range(len(names)):
        c = b.replace(b[5:11], names[i])
        d = open(f'Output/ReadyToSend/letter_for_{names[i]}.txt', mode='w')
        d.write(c)


"""
#screen settings
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Title')
screen.tracer(0)
screen.colormode(255)




screen.exitonclick()
"""