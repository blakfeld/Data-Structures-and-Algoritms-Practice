#!/usr/bin/env python
"""
binary_search_sorted_array.py:
    Implement binary search of a sorted array of integers

Author: Corwin Brown <blakfeld@gmail.com>
"""
from __future__ import print_function

import sys

import utils


def binary_search(list_to_search, num_to_find):
    """
    Perform Binary Search on a sorted array of ints.

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
            return mid, num_to_find

        if num_to_find > list_to_search[mid]:
            first = mid + 1
        else:
            last = mid - 1

    return None, None


def main():
    """
    Main.
    """
    list_to_search = sorted(utils.get_unique_random_list())
    print(binary_search(list_to_search, 30))


if __name__ == '__main__':
   sys.exit(main())
