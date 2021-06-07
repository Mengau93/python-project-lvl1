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
