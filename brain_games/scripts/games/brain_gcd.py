"""Start simple gcd  game."""
import prompt
from brain_games.scripts.user_welcome import welcome_user
from brain_games.scripts.calculations import gcd, two_random_nums


def main():
    """Start the game."""
    name = welcome_user()
    print('Find the greatest common divisior of given numbers. ')
    summary_counter = 0
    correct_counter = 0
    while summary_counter < 3:
        data = two_random_nums()
        correct_ans = gcd(*data)
        print('Question: {0} {1}'.format(*data))
        ans = prompt.string('Your answer: ')
        if not ans.isdigit():
            print("Incorrect answer")
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
