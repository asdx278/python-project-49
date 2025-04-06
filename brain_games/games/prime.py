import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def game():
    question = random.randrange(100)
    divider = 2
    if question < 2:
        correct_answer = 'no'
        return question, correct_answer
    while divider <= question / 2:
        if question % divider == 0:
            correct_answer = 'no'
            return question, correct_answer
        divider += 1
    correct_answer = 'yes'
    return question, correct_answer