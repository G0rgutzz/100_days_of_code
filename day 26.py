import random
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
