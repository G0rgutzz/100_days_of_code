from day_14_game_data import data
import random
# import os


def char_choice():
    first_char = random.choice(data)
    second_char = random.choice(data)
    print(f"Compare A: {first_char['name']}, a {first_char['description']} from {first_char['country']} \n"
          f"VS\nAgainst B: {second_char['name']}, a {second_char['description']} from {second_char['country']}")
    choice = input("Who has more followers. Type 'A' or 'B':").upper()
    if choice == 'A':
        choice_p = first_char['follower_count']
    elif choice == 'B':
        choice_p = second_char['follower_count']
    if first_char['follower_count'] > second_char['follower_count']:
        winner = first_char['follower_count']
    else:
        winner = second_char['follower_count']
    return winner, choice_p


def game():
    lost = False
    score = 0
    while lost is False:
        a = char_choice()
        tmp_ch = a[1]
        tmp_w = a[0]
        if tmp_w == tmp_ch:
            score += 1
            # os.system('cls')  # doesn't work in python
            print(f"You're right, current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            lost = True


game()
