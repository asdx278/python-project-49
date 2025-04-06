import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
def game():
    question = random.randrange(100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer