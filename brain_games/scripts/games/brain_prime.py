"""Start simple progression game."""
import prompt
import random
from brain_games.scripts.user_welcome import welcome_user
from brain_games.scripts.calculations import is_prime


def main():
    """Start the game."""
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no". ')
    summary_counter = 0
    correct_counter = 0
    while summary_counter < 3:
        data = random.randint(2, 50)
        correct_ans = 'yes' if is_prime(data) else 'no'
        print('Question:', data)
        ans = prompt.string('Your answer: ')
        if ans == correct_ans:
            print('Correct!')
            correct_counter += 1
        else:
            print('"{0}" is wrong answer ;(.'.format(ans), end=' ')
            print('Correct answer was "{0}"'.format(correct_ans))
            break
        summary_counter += 1
    if correct_counter == 3:
        print('Congratulations, {0}'.format(name))


if __name__ == '__main__':
    main()
