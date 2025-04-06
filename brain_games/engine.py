import prompt


def engine(game):
    COUNT_ROUND = 3
    user_score = 0
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.RULE)
    for _ in range(COUNT_ROUND):
        question, correct_answer = game.game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            user_score += 1
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \
                  \'{correct_answer}\'')
            print(f'Let\'s try again, {user_name}!')
            break
    if user_score == 3:
        print(f'Congratulations, {user_name}!')