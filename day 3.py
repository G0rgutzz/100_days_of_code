
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride a rollercoaster")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Ticket costs $7")
    else:
        print("Ticket costs $12")
else:
    print("You can't ride a rollercoaster")
'''
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
names = [name1, name2]
total1 = 0
total2 = 0
for k in range(len(names)):
    for i in range(len(names[k])):
        if names[k].upper()[i] == "T":
            total1 += 1
        if names[k].upper()[i] == "R":
            total1 += 1
        if names[k].upper()[i] == "U":
            total1 += 1
        if names[k].upper()[i] == "E":
            total1 += 1
            total2 += 1
        if names[k].upper()[i] == "L":
            total2 += 1
        if names[k].upper()[i] == "O":
            total2 += 1
        if names[k].upper()[i] == "V":
            total2 += 1


value = total1 * 10 + total2

if value < 10 or value > 90:
    print(f"Your score is {value}, you go together like coke and mentos.")
elif (value > 40) and (value < 50):
    print(f"Your score is {value}, you are alright together.")
else:
    print(f"Your score is {value}.")'''
