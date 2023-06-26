
'''
n = input(str("What is your name: "))
print(len(n))

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
temp = a
a = b
b = temp

# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b) '''

print('Welcome to the Band Name Generator.')
a = input(str("What's the name of the city you grew up in?\n"))
b = input(str("What's your pet's name?\n"))
print("Your band name would be", a + " " + b)
