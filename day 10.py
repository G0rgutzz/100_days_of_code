import numpy
import random
# functions with outputs

'''
def format_name():
    name = input("what is your name? ")
    # print(name.title())
    return name.title()


format_name()  # prints nothing as there is no print
'''
# calculator program


def add(n1, n2):
    return n1+n2


def subtraction(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        print("you can't divide by 0")
    else:
        return n1 / n2


def power(n1, n2):
    return n1**n2


operations = {
    "+": add, "-": subtraction, "*": multiply, "/": divide, "^": power
}
num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))
for item in operations:
    print(item, operations[item])
symbol = input("Pick an operation from the line above: ")
answer = operations[symbol](num1, num2)
print(f"{num1} {symbol} {num2} = {answer}")
symbol = input("Pick another operation: ")
num3 = int(input("What's another number? "))
answer1 = operations[symbol](answer, num3)
print(f"{answer} {symbol} {num3} = {answer1}")

