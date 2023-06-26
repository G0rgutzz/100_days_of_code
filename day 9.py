import random
from os import system
'''
programming_dictionary = {
    "Bug": "An error in program that prevents it from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
}
for key in programming_dictionary:
    print(programming_dictionary[key])
programming_dictionary["Loop"] = "The action of doing something over and over again"
empty_dict = {}
empty_dict["Bug"] = "A moth in your computer"  # adding/editing items to dictionary
programming_dictionary = {}  # wiping everything from the dictionary

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
# second solution
for key in student_scores:
    score = student_scores[key]
    if score > 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = "Exceeds Expectations"
    elif score > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)
# mine solution

a = []
b = []
c = []
for key in student_scores:
    a.append(student_scores[key])
    c.append(key)
print(c)
for item in a:
    if item > 90:
        b.append("Outstanding")
    elif item > 80:
        b.append("Exceeds Expectations")
    elif item > 70:
        b.append("Acceptable")
    else:
        b.append("Fail")

for i in range(0, len(a)):
    student_grades[c[i]] = b[i]
print(student_grades)


# Nesting dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 13}
}  # cities visited in the country
print(travel_log["France"]["cities_visited"][1])  # calling specific item from the dictionary
# Nesting dictionary in a list
travel_log = [
     {"country": "France",
      "cities_visited": ["Paris", "Lille", "Dijon"],
      "total_visits": 12
      },
     {"country": "Germany",
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
      "total_visits": 13
      }
]  # cities visited in the country


def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
'''
print("Welcome to the secret auction program")


def bidder():
    bidders = {}
    others = 'yes'
    while others == 'yes':
        name = input("What is your name: ")
        bid = int(input("What is your bid: $"))
        bidders[name] = bid
        others = input("Are there any other bidders? Type 'yes' or 'no'")
        system('cls')  # doesn't work in pycharm
    print(f"The winner is {max(bidders, key=bidders.get)} with a bid of ${bidders[max(bidders, key=bidders.get)]}")
    # prints key with max value and value of this key with second argument
    # key=bidders.get - without it function will return last value in the dictionary


bidder()
