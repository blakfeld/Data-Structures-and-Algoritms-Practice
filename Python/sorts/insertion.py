"""
insertion.py -- Insertion Sort algorithm
"""

from util import swap, generate_list_of_random_numbers


def insertion(to_sort):
    """
    Perform insertion sort.

    Args:
        to_sort (list):     list to sort.

    Returns:
        list
    """

    for i in xrange(1, len(to_sort)):
        j = i
        while j > 0 and to_sort[j - 1] > to_sort[j]:
            to_sort = swap(to_sort, j, j - 1)
            j -= 1

    return to_sort

if __name__ == '__main__':
    rand_list = generate_list_of_random_numbers(10000)

    print insertion(rand_list)
