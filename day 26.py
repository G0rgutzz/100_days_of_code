import random

import pandas as pd
"""
# few exercises to learn list comprehensions
numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
name = "Grzegorz"
letters_list = [letter for letter in name]
n = range(1, 5)
new_n = [2*item for item in range(1,5)]
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
caps_names = [name.upper() for name in names if len(name)>5]

# dictionary comprehension
students_scores = {name:random.randint(1, 100) for name  in names}
print(students_scores)
passed_students = {name:value for (name, value) in students_scores.items() if value>70}
print(passed_students)

# coding exercise
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result = {word:len(word) for word in words}
print(result)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 78, 90]
}

student_df = pandas.DataFrame(student_dict)
# print(student_df)
# looping a data frame
for (key, value) in student_df.items():
    print(value)

# looping through data frame rows
for (index, row) in student_df.iterrows():
    print(row)
"""
# NATO alphabet project
alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
letter_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()}
# print(letter_dict)
#letter_dict_test1 = alphabet.to_dict()  # not the same format as above
# print(letter_dict_test1)
word = input("Input a word: ").upper()
word_list = []
for x in word:
    print(letter_dict[x])
    word_list.append(letter_dict[x])

