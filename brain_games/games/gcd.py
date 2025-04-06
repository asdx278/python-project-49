import math
import random

RULE = 'Find the greatest common divisor of given numbers.'


def game():
    first_number = random.randrange(10)
    second_number = random.randrange(10)
    question = f'{first_number} {second_number}'
    return question, str(math.gcd(first_number, second_number))

