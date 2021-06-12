"""Start simple gcd game."""
import prompt
from brain_games.scripts.user_prompts import welcome_user
from brain_games.scripts.user_prompts import print_wrong
from brain_games.scripts.user_prompts import print_correct
from brain_games.scripts.calculations import gcd, two_random_nums


def question_generate():
    data = two_random_nums()
    correct_ans = gcd(*data)
    return data, str(correct_ans)


def main():
    """Start the game."""
    name = welcome_user()
    print('Find the greatest common divisior of given numbers. ')
    summary_counter = 0
    correct_counter = 0
    while summary_counter < 3:
        data, correct_ans = question_generate()
        print('Question: {0} {1}'.format(*data))
        ans = prompt.string('Your answer: ')
        if ans == correct_ans:
            correct_counter = print_correct(correct_counter)
        else:
            print_wrong(name, ans, correct_ans)
            break
        summary_counter += 1
    if correct_counter == 3:
        print('Congratulations, {0}!'.format(name))


if __name__ == '__main__':
    main()
