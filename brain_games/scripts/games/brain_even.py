"""Start simple even-odd game."""
import prompt
import random
from brain_games.scripts.user_prompts import welcome_user
from brain_games.scripts.user_prompts import print_wrong
from brain_games.scripts.user_prompts import print_correct


def question_generate():
    x = random.randint(0, 100)
    correct_ans = 'yes' if x % 2 == 0 else 'no'
    return x, correct_ans


def main():
    """Start the game."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    summary_counter = 0
    correct_counter = 0
    while summary_counter < 3:
        x, correct_ans = question_generate()
        print('Question: {0}'.format(x))
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
