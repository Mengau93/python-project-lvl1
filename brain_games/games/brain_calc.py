"""Start simple calculator game."""
import prompt
from brain_games.scripts.user_welcome import welcome_user
from brain_games.scripts.calculations import randomization, two_args_calc


def main():
    """Start the game."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    summary_counter = 0
    correct_counter = 0
    while summary_counter < 3:
        data = randomization()
        correct_ans = two_args_calc(data)
        print('Question: {0}{1}{2}'.format(*data))
        ans = prompt.string('Your answer: ')
        if not ans.isdigit():
            print('Incorrect answer!')
        elif int(ans) == correct_ans:
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
