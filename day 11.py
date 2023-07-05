import random


def blackjack():
    cards_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # cards values,
    # to be tied with their names later
    dealer_value = 0  # value of the dealer's cards
    player_value = 0  # value of the player's cards
    cards_amount = 2  # to be used later
    bet = 0  # same as above
    turn = 1  # same as above
    play = True  # states if the player wants to play more, initially True
    while play is True:
        if turn == 1:
            for i in range(0, cards_amount):
                dealer_value += random.choice(cards_values)
                player_value += random.choice(cards_values)
            print(f"Dealer value is {dealer_value}\nYour value is {player_value}.")
            if player_value == 21:
                print(f"Congratulations, you've hit a blackjack.")
        else:
            dealer_value += random.choice(cards_values)
            player_value += random.choice(cards_values)
            print(f"Dealer value is {dealer_value}\nYour value is {player_value}.")
        if dealer_value >= 21 or player_value >= 21:
            if player_value > 21 and dealer_value > 21:
                print(f"You draw with dealer with {dealer_value} points after {turn} turns.")
                exit()
            elif player_value > 21 or dealer_value == 21:
                print(f"Dealer won with {dealer_value} points. You lost with {player_value} after {turn} turns.")
                exit()
            else:
                print(f"You won with {player_value} points. Dealer lost with {dealer_value} after {turn} turns.")
                exit()
        tmp1 = input("Do you want to play next turn? Type y for 'yes'")
        if tmp1 == 'y':
            play = True
            turn += 1
        else:
            play = False

    if play is False:
        if dealer_value > player_value:
            print(f"Dealer won with {dealer_value} points. You lost with {player_value} after {turn} turns.")
        elif dealer_value == player_value:
            print(f"You draw with dealer with {dealer_value} points after {turn} turns.")
        else:
            print(f"You won with {player_value} points. Dealer lost with {dealer_value} after {turn} turns.")


blackjack()
