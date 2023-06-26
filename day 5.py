import random
'''
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
# faster way
av = int(round(sum(student_heights)/len(student_heights), 0))
print(av)
# longer way
s = 0
for n in student_heights:
    s += n
ah = round(s/len(student_heights), 0)
print(ah)
# project
'''


def Password_Generator():
    print('Welcome to PyPassword Generator')
    nl = int(input('How many letters would you like in your password? \n'))
    ns = int(input('How many symbols would you like? \n'))
    nm = int(input('How many numbers would you like? \n'))

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pw = []
    password = ''
    for i in range(0, nl+nm+ns):
        pw.append(random.choice(letters))
    if nm > 0:
        for j in range(0, nm):
            pw[random.randint(0, len(pw)-1)] = str(random.choice(numbers))
    if ns > 0:
        for k in range(0, ns):
            pw[random.randint(0, len(pw)-1)] = str(random.choice(symbols))
    # random.shuffle(pw)  # additionally shuffles the list in random way
    for i in range(0, nl+nm+ns):
        password += pw[i]
    print(f"Your password is: {password}")


Password_Generator()
