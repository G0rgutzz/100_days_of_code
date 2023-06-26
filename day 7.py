import random


def hangman():
    wordlist = ['ardvark', 'baboon', 'camel']
    word = random.choice(wordlist)

    guess = '_'*len(word)
    guess_tmp = ''
    health = 6
    x = []
    for i in range(0, len(word)):
        x.append('_')
    while health > 0:
        a = input("Guess a letter: \n").lower()
        for i in range(0, len(word)):
            if word[i] == a:
                x[i] = a

        for el in x:
            guess_tmp += el

        if guess_tmp == guess:
            health -= 1
            print(f"you didn\'t guessed any letter. You lose 1 health. Health remaining: {health}")

        guess = guess_tmp
        print(f"you word is {guess}")
        guess_tmp = ''

        if guess == word:
            print(f"You have won with {health} health remaining")
            exit()

    if health == 0:
        print("You lost :'(")
        print(guess)


hangman()
