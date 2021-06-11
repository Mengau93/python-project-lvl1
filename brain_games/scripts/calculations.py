"""Calculation functions library"""
import random


def randomization():
    """Returns random data as tuple
    (x, sign, y), where:
        x and y - random number from 0 to 100,
        sign - one of three signs - '+', '-', '*'"""
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    sign = random.choice(['+', '-', '*'])
    return (x, sign, y)


def two_args_calc(data):
    """Takes a tuple of three elements (x, sign, y).
    Returns the value of x <sign> y.
    For example if we have a tuple (2, '+', 5), then
    function will return 7"""
    if data[1] == '+':
        return data[0] + data[2]
    elif data[1] == '-':
        return data[0] - data[2]
    elif data[1] == '*':
        return data[0] * data[2]
    else:
        return 'Error!'


def gcd(x, y):
    """Returns a GCD of two numbers - x and y"""
    while x * y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return x + y


def two_random_nums():
    """Returns a tuple of two random numbers from 0 to 100"""
    return random.randint(0, 100), random.randint(0, 100)


def arythm_progression_generate():
    """
    Returns a list of arythmectic progression
    with random number of elements and random numbers.
    Start number from 0 to 50.
    Common Difference from 1 to 10.
    """
    start = random.randint(0, 50)
    com_diff = random.randint(1, 10)
    res = []
    count = random.randint(5, 15)
    for i in range(count):
        res.append(start)
        start += com_diff
    return res


def is_prime(x):
    """
    Return True if x is Prime
    and False if x is not Prime
    """
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
