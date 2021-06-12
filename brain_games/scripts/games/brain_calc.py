"""Start simple calculator game."""
import prompt
from brain_games.scripts.user_prompts import welcome_user
from brain_games.scripts.user_prompts import print_wrong
from brain_games.scripts.user_prompts import print_correct
from brain_games.scripts.calculations import randomization, two_args_calc


def question_generate():
    data = randomization()
    correct_ans = two_args_calc(data)
    return data, str(correct_ans)


def main():
    """Start the game."""
    name = welcome_user()
    print('What is the result of the expression? ')
    summary_counter = 0
    correct_counter = 0
    while summary_counter < 3:
        data, correct_ans = question_generate()
        print('Question: {0}{1}{2}'.format(*data))
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
