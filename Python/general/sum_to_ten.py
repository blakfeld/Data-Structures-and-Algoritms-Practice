#!/usr/bin/env python
"""
sum_to_ten.py
    Given a list of ints, return a pair of numbers in the
    array that sum to ten.

Author: Corwin Brown <blakfeld@gmail.com>
"""
from __future__ import print_function

import sys

import utils


TARGET_INT = 8


def find_sum_to_ten(list_to_search):
    """
    Given a list of ints, return a pair that adds up
        to a gobal target.

    Args:
        list_to_search (list):  The list to search.

    Returns:
        tuple
    """
    diff_from_ten = {}
    for item in list_to_search:
        if item in diff_from_ten:
            return (item, diff_from_ten[item])
        diff_from_ten[TARGET_INT - item] = item


def main():
    """
    Main.
    """
    list_to_search = utils.get_random_list()
    left, right = find_sum_to_ten(list_to_search)
    print('{0} + {1} = {2}'.format(left, right, TARGET_INT))


if __name__ == '__main__':
   sys.exit(main())
