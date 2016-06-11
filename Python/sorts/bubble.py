"""
bubble.py -- Bubble Sort
"""

from util import swap, generate_list_of_random_numbers


def bubble_sort(to_sort):
    """
    Implement Bubble Sort.

    Args:
        to_sort (list):     List to sort.
    """

    list_length = len(to_sort) - 1
    for i in xrange(0, len(to_sort), 1):
        for j in xrange(0, len(to_sort) - i, 1):
            if j + 1 > list_length:
                break

            if to_sort[j] > to_sort[j + 1]:
                to_sort = swap(to_sort, j, j + 1)

    return to_sort


if __name__ == '__main__':
    rand_list = generate_list_of_random_numbers(10000)

    print bubble_sort(rand_list)
