""" test class from the lesson
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0
        print("new user was created")
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User('001', 'Gork')
user2 = User('002', 'Mork')
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
"""
from day17_data import question_data
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        query = self.q_list[self.q_number]
        self.q_number += 1
        u_answer = input(f"Q.{self.q_number}: {query.text} (True/False)")
        self.check_answers(u_answer, query.answer)

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def check_answers(self, u_answer, answer):
        if u_answer.lower() == answer.lower():
            self.score += 1
            print("That's correct")
        else:
            print("That's wrong")
        print(f"Your score is {self.score}/{self.q_number}\n")


question_bank = []
answer_bank = []
for key in question_data:
    question = key['text']
    value = key['answer']
    question_bank.append(Question(text=question, answer=value))
quiz = QuizBrain(question_bank)

while quiz.still_has_questions() is True:
    quiz.next_question()
else:
    print("You've completed the quiz")
    print(f"Your final score is: {quiz.score}/{quiz.q_number}")

