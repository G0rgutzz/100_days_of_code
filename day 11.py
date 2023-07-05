import random
tmp_pv = 0
tmp_dv = 0


def deal_card():
    cards_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # cards values,
    # to be tied with their names later
    card = random.choice(cards_values)
    return card


def blackjack():
    dealer_cards = []  # dealer cards
    player_cards = []  # player cards
    dealer_value, player_value = 0, 0
    win_d, win_p = 0, 0  # amount of dealer and player wins
    cards_amount = 2  # to be used later
    bet = 0  # same as above
    turn = 1  # same as above
    play = True  # states if the player wants to play more, initially True
    while play is True:
        if turn == 1:
            for i in range(0, cards_amount):
                dealer_cards.append(deal_card())
                player_cards.append(deal_card())
            dealer_value = sum(dealer_cards)
            player_value = sum(player_cards)
            print(f"Dealer value is {dealer_value}\nYour value is {player_value}.")
            if player_value == 21 or dealer_value == 21:
                if player_value == 21:
                    print(f"Congratulations, you've hit a blackjack.")
                    win_p += 1
                    return win_p, win_d
                elif dealer_value == 21:
                    print(f"Dealer hit a blackjack.")
                    win_d += 1
                    return win_p, win_d
        else:
            dealer_cards.append(deal_card())
            player_cards.append(deal_card())
            if (dealer_cards[-1] == 11 and sum(dealer_cards) > 21) or \
                    (player_cards[-1] == 11 and sum(player_cards) > 21):
                if (dealer_cards[-1] == 11 and sum(dealer_cards) > 21) and \
                        (player_cards[-1] == 11 and sum(player_cards) > 21):
                    dealer_cards[-1] = 1
                    player_cards[-1] = 1
                elif dealer_cards[-1] == 11 and sum(dealer_cards) > 21:
                    dealer_cards[-1] = 1
                elif player_cards[-1] == 11 and sum(player_cards) > 21:
                    player_cards[-1] = 1
            dealer_value = sum(dealer_cards)
            player_value = sum(player_cards)
            print(f"Dealer value is {dealer_value}\nYour value is {player_value}.")

        if dealer_value >= 21 or player_value >= 21:
            if player_value > 21 and dealer_value > 21:
                print(f"You draw with dealer with {dealer_value} points after {turn} turns.")
                return win_p, win_d
            elif player_value > 21 or dealer_value == 21:
                print(f"Dealer won with {dealer_value} points. You lost with {player_value} after {turn} turns.")
                win_d += 1
                return win_p, win_d
            else:
                print(f"You won with {player_value} points. Dealer lost with {dealer_value} after {turn} turns.")
                win_p += 1
                return win_p, win_d

        tmp1 = input("Do you want to play next turn? Type y for 'yes'")
        if tmp1 == 'y':
            play = True
            turn += 1
        else:
            play = False

    if play is False:
        if dealer_value > player_value:
            print(f"Dealer won with {dealer_value} points. You lost with {player_value} after {turn} turns.")
            win_d += 1
            return win_p, win_d
        elif dealer_value == player_value:
            print(f"You draw with dealer with {dealer_value} points after {turn} turns.")
            return win_p, win_d
        else:
            print(f"You won with {player_value} points. Dealer lost with {dealer_value} after {turn} turns.")
            win_p += 1
            return win_p, win_d


counter = 0
next_game = 'y'
while next_game == 'y':
    a = blackjack()
    tmp_pv += a[0]
    tmp_dv += a[1]
    print(f"Overall score player vs dealer is {tmp_pv}:{tmp_dv}")
    next_game = input("Do you want to play another game? Type y for 'yes'.")
    print("\n")
    counter += 1
else:
    print("Thank you for playing")
