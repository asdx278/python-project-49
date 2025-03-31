import prompt
import random


def check_user_answer(user_answer, question_number):
    if question_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    if user_answer == correct_answer:
        return True
    else:
        return False


def game():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    user_score = 0
    while user_score < 3:
        min_number = random.randint(0, 10)
        max_number = random.randint(100, 200)
        rand_number = random.randint(min_number, max_number)
        print(f'Question:{rand_number}')
        user_answer = prompt.string('Your answer: ')
        if check_user_answer(user_answer, rand_number):
            user_score += 1
            print('Correct!')
        else:
            if user_answer == 'yes':
                print(f'\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
                break
            else:
                print(f'\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
                break
    if user_score == 3:
        print(f'Congratulations, {user_name}')


def main():
    game()

    if __name__ == "__main__":
        main()
