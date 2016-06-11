"""
util.py -- Common functions to be used by various sorting algorithms.
"""

import random


def swap(l, i, j):
    """
    Swap the index i with the index j in list l.

    Args:
        l (list):   list to perform the operation on.
        i (int):    left side index to swap.
        j (int):    Right side index to swap.

    Returns:
        list
    """

    l[i], l[j] = l[j], l[i]

    return l


def generate_list_of_random_numbers(length):
    """
    Generate a list of random numbers.

    Args:
        length (int):   The length of the list.

    Returns:
        list
    """

    rand_nums = []
    for i in xrange(0, length):
        rand_nums.append(random.randrange(0, 99))

    return rand_nums
