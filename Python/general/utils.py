"""
util.py:
    Utility functions for practice. This will help keep me from
    having to continuously write bits of boilerplate
"""
from __future__ import print_function

import random


def get_random_list(length=100, max_num=10):
    """
    Generate a list containing random numbers.

    Args:
        length (int):   The length of the list to generate.
        max_num (int):  The largest number to include in the list.

    Returns:
        list
    """
    return [random.randrange(1, max_num, 1) for _ in range(length)]


def get_unique_random_list(length=100, max_num=100):
    """
    Generate a list containing unique random numbers. `length` must
    be larger than `max_num`.

    Args:
        length (int):   The length of list to return.
        max_num (int):  The largest number to place in the list.

    Returns:
        list

    Raises:
        ValueError if `max_num` is larger than `length`.
    """
    if max_num > length:
        raise ValueError('max_num cannot be larger than length')

    return random.sample(xrange(max_num), length)


def rotate_list(list_to_rotate, amount):
    """
    Rotate a list.

    Args:
        list_to_rotate (list):  The list we wish to rotate.
        amount (int):           How much to rotate the list.

    Returns:
        list
    """
    return list_to_rotate[amount:] + list_to_rotate[:amount]


if __name__ == '__main__':
    print(get_random_list())

