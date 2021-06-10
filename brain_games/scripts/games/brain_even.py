"""Start simple even-odd game."""
import prompt
import random


def main():
    """Start the game."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no"')
    summary_counter = 0
    correct_answers = 0
    while summary_counter < 3:
        x = random.randint(0, 100)
        print('Question: {0}'.format(x))
        ans = prompt.string('Your answer: ')
        if x % 2 == 0 and ans == 'yes' or x % 2 == 1 and ans == 'no':
            print('Correct!')
            correct_answers += 1
        else:
            if ans == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'")
            elif ans == 'no':
                print("'no' is wrong answer ;(. Correct answer was 'yes'")
            else:
                print('Your answer is wrong ;(.')
            break
        summary_counter += 1
    if correct_answers == 3:
        print('Congratulations, {0}'.format(name))


if __name__ == '__main__':
    main()
