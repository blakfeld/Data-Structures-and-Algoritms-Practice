#!/usr/bin/env python
"""
common_elements.py:
    Find the common elements of 2 int arrays.

Author: Corwin Brown <blakfeld@gmail.com>
"""
from __future__ import print_function

import sys
from collections import defaultdict


def find_common_elements(list_a, list_b):
    """
    Find the common elements in two arrays.

    Args:
        list_a (list):  The first list to compare.
        list_b (list):  The second list to compare.

    Returns:
        list
    """
    if len(list_a) > len(list_b):
        larger, smaller = list_a, list_b
    else:
        larger, smaller = list_b, list_a

    return [elem for elem in smaller if elem in set(larger)]


def main():
    """
    Main.
    """
    list_a = [1, 2, 5, 9, 7, 0, 4]
    list_b = [5, 3, 1, 6, 9, 8, 7, 3, 2]
    print(find_common_elements(list_a, list_b))


if __name__ == '__main__':
   sys.exit(main())
