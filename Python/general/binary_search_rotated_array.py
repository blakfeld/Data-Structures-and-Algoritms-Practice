#!/usr/bin/env python
"""
binary_search_rotated_array.py

Author: Corwin Brown <blakfeld@gmail.com>
"""
from __future__ import print_function

import sys

import utils


def binary_search(list_to_search, num_to_find):
    """
    Perform a Binary Search on a rotated array of ints.

    Args:
        list_to_search (list):  The list to search.
        num_to_find (int):      The int to search for.

    Returns:
        tuple: (index, value)
    """
    first = 0
    last = len(list_to_search) - 1
    while first <= last:
        mid = (first + last) // 2
        if list_to_search[mid] == num_to_find:
            return mid, list_to_search[mid]

        # Is first half sorted?
        if list_to_search[first] <= list_to_search[mid]:
            # If first and mid are less than num_to_find, Search the
            #   first half, else search the second half.
            if all([list_to_search[first] <= num_to_find,
                    list_to_search[mid] >= num_to_find]):
                last = mid - 1
            else:
                first = mid + 1

        # If the second half is sorted.
        else:
            # If last and mid are less than num_to_find, Search the
            # second half, else search the first half.
            if all([list_to_search[mid] <= num_to_find,
                    list_to_search[last] <= num_to_find]):
                first = mid + 1
            else:
                last = mid - 1

    return None, None


def main():
    """
    Main.
    """
    list_to_search = utils.rotate_list(sorted(utils.get_unique_random_list()), 10)
    print(binary_search(list_to_search, 30))


if __name__ == '__main__':
   sys.exit(main())
