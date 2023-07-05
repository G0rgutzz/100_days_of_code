import random

# number guessing game


def difficulty():  # function that sets difficulty level
    diff = input("Choose a difficulty, type 'easy' or 'hard'")
    if diff == 'easy':
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number")
        return attempts
    elif diff == 'hard':
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number")
        return attempts


def guess():
    a = difficulty()
    number = random.randint(1, 100)
    for i in range(0, a):
        user_number = int(input("Make a guess:"))
        if user_number > number:
            print("Too high\nGuess again")
            a += -1
            print(f"You have {a} attempts remaining")
        elif user_number < number:
            print("Too low\nGuess again")
            a += -1
            print(f"You have {a} attempts remaining")
        elif user_number == number:
            print(f"Congratulations, you guessed the number with {a} attempts remaining")
            exit()
        if a == 0:
            print("You've run out of attempts. You lose")


print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
guess()
