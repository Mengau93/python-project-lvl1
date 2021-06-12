"""Welcome the user."""
import prompt


def welcome_user():
    """Return username after welcome him."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def print_wrong(name, ans, correct_ans):
    """Ends the game."""
    print(f"'{ans}' is wrong answer ;(. Correct answer was '{correct_ans}'.")
    print(f"Let's try again, {name}!")


def print_correct(correct_counter):
    """Adds one more correct answer to counter"""
    print('Correct!')
    return correct_counter + 1


if __name__ == '__main__':
    welcome_user()
