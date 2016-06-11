"""
selection.py -- Selection sort algorithm.
"""

from util import swap, generate_list_of_random_numbers


def selection(to_sort):
    """
    Perform selection sort.

    Args:
        to_sort (list):     List to Sort,
    """

    list_length = len(to_sort)
    for i in xrange(0, list_length):
        min_index = i
        for j in xrange(i, list_length):
            if to_sort[j] < to_sort[min_index]:
                min_index = j

        if min_index != i:
            to_sort = swap(to_sort, i, min_index)

    return to_sort


if __name__ == '__main__':
    rand_list = generate_list_of_random_numbers(10000)

    print selection(rand_list)
