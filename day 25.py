import pandas as pd
import random
import turtle

"""code for the 227 and 228 video"""
"""weather = pd.read_csv('weather_data.csv')
temperature = weather['temp']
print(temperature)

new_dict = weather.to_dict()  # turns dataframe into a dictionary
print(new_dict)
new_list = weather['temp'].to_list()  # turns column from the dataframe into a list
print(new_list)
temp_avg = temperature.mean()  # average temp
print(temp_avg)
temp_max = temperature.max()  # max temp
print(temp_max)
print(weather['condition'])
print(weather.condition)  # alternative version of the column calling. Every column name is an attribute to be used
# data in rows
print(weather[weather.day == 'Monday'])  # shows data from monday
print(weather[weather.temp == weather.temp.max()])  # shows data from the day with max temperature
print(weather[weather.day == 'Monday'].temp*1.8+32)  # converting monday temp to retarded units

#creating dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
df = pd.DataFrame(data_dict)
print(df)
# creating csv file for squirrel count based on their fur color

squirells = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_colors = pd.DataFrame(squirells['Primary Fur Color'].value_counts()).reset_index()
fur_colors.to_csv('squirells_fur_colors_count.csv')
"""

"""us state quiz game"""

screen = turtle.Screen()
screen.title('US states game')  # title
screen.setup(height=600, width=700)
image = 'blank_states_img.gif'
turtle.addshape(image)  # adding image shape to turtle
turtle.shape(image)  # displaying added shape

def get_mouse_click_coor(x, y):  # function to get mouse click coordinates
    print(x, y)


# reading state names and their positions on the image
states = pd.read_csv('50_states.csv')
# turtle.onscreenclick(get_mouse_click_coor)
t = turtle.Turtle()
t.hideturtle()
correct = 0
states_to_learn = states.state.to_list()

for i in range(0, 50):
    answer = screen.textinput(title=f'{i}/50 states guessed',
                          prompt="What's another state name?")
    if answer == 'Exit':
        break
    for j in range(0, 50):
        if answer.lower() == states.state[j].lower():
            correct += 1
            t.penup()
            t.goto(states.x[j], states.y[j])
            t.write(arg=f'{states.state[j]}', align='center',
                       font=('Times New Roman', 12, 'normal'))
            states_to_learn.remove(states.state[j])

screen.textinput(title=f'Test is finished, you guessed {correct}/50 states correctly',
                 prompt='write anything to accept', )
print(f'Test is finished, you guessed {correct}/50 states correctly')
to_learn = pd.DataFrame(states_to_learn)
to_learn.to_csv('states_to_learn.csv')
turtle.mainloop()  # keeps the screen open even though code has stopped running - alternative to exitonclick
