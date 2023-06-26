import random


def cipher():
    next_round = True
    while next_round:
        new_word = ''
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        print("Hello, welcome to the cipher")
        coding = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        sentence = input("Type your message: \n")
        num = int(input("Type the shift number: \n"))
        # another solution
        '''
        text = ''
        if coding == 'decode':
            num *= -1
        for letter in sentence:
            position = alphabet.index(letter)
            new_pos = position + num
            new_letter = alphabet[new_pos]
            text += new_letter
        print(f"The {coding}d text is: {text}")
        '''
        # mine solution
        if num > len(alphabet):
            num = num % len(alphabet)
        if coding == 'encode':
            for i in range(0, len(sentence)):
                for j in range(0, len(alphabet)):
                    if sentence[i] == (alphabet[j]):
                        if j+num >= len(alphabet):
                            new_word += alphabet[j+num-len(alphabet)]
                        elif j+num < len(alphabet):
                            new_word += alphabet[j+num]
        elif coding == 'decode':
            for i in range(0, len(sentence)):
                for j in range(0, len(alphabet)):
                    if sentence[i] == (alphabet[j]):
                        new_word += alphabet[j-num]
        print(f"The {coding}d text is: {new_word}")
        another = input("Type 'yes' if you want to continue. Otherwise type 'no' ")
        if another == 'no':
            next_round = False
            print("Bye")


cipher()

'''
def prime_checker(number):
    a = 0
    b = 0
    for i in range(2, number):
        if number % i == 0:
            a += 1
        else:
            b += 1
    if a == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
'''
