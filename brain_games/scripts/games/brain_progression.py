"""Start simple progression game."""
import prompt
import random
from brain_games.scripts.user_prompts import welcome_user
from brain_games.scripts.user_prompts import print_wrong
from brain_games.scripts.user_prompts import print_correct
from brain_games.scripts.calculations import arythm_progression_generate as apg


def question_generate():
    data = apg()
    hidden_index = random.randint(0, len(data) - 1)
    correct_ans = data[hidden_index]
    data[hidden_index] = ".."
    return data, str(correct_ans)


def main():
    """Start the game."""
    name = welcome_user()
    print('What number is missing in the progression? ')
    summary_counter = 0
    correct_counter = 0
    while summary_counter < 3:
        data, correct_ans = question_generate()
        print('Question:', *data)
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
