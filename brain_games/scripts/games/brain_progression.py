"""Start simple progression game."""
import prompt
import random
from brain_games.scripts.user_welcome import welcome_user
from brain_games.scripts.calculations import arythm_progression_generate as apg


def main():
    """Start the game."""
    name = welcome_user()
    print('What number is missing in the progression? ')
    summary_counter = 0
    correct_counter = 0
    while summary_counter < 3:
        data = apg()
        hidden_index = random.randint(0, len(data) - 1)
        correct_ans = data[hidden_index]
        data[hidden_index] = ".."
        print('Question:', *data)
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
