"""Welcome the user."""
import prompt


def welcome_user():
    """Welcome user with his name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


if __name__ == '__main__':
    welcome_user()
