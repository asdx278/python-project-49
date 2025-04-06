import random

RULE = 'What number is missing in the progression?'


def game():
    base_progression = random.randint(1, 10)
    start_progression = random.randint(1, 100)
    length_progression = random.randint(5, 15)
    elements_progression = [start_progression]
    for i in range(length_progression):
        new_element = elements_progression[i] + base_progression
        elements_progression.append(new_element)
    correct_answer = random.choice(elements_progression)
    question = ' '.join(str(elem) for elem in elements_progression)
    question = question.replace(str(correct_answer), '..', 1)

    return question, str(correct_answer)
