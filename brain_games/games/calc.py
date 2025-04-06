import random

RULE = 'What is the result of the expression?'


def game():
    first_number = random.randrange(100)
    second_number = random.randrange(100)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    question = f'{first_number} {operator} {second_number}'
    if operator == '+':
        correct_answer = first_number + second_number
    elif operator == '-':
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return question, str(correct_answer)