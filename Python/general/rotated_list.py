#!/usr/bin/env python
"""
rotated_list.py
    Given 2 integer arrays, determine of the 2nd array is a rotated
    version of the 1st array.
    Ex:
        Original Array A = [1, 2, 3, 4, 5, 6, 7, 8]
        Rotated Array B = [5, 6, 7, 8, 1, 2, 3]

Author: Corwin Brown <blakfeld@gmail.com>
"""
from __future__ import print_function

import sys


def is_rotated_list(list_a, list_b):
    """
    Check if `list_b` is a rotated version of `list_a`. To do this,
        concat `list_a` with `list_a`, then check if `list_b` is
        a sublist of it.

    Args:
        list_a (list):  The "primary" list.
        list_b (list):  The list to check if is rotated.

    Returns:
        bool
    """
    if len(list_a) != len(list_b):
        return False

    double_list = list_a + list_a
    
    j = 0
    for i in range(len(double_list)):
        if double_list[i] == list_b[j]:
            j += 1
        else:
            j = 0

        if j == (len(list_b) - 1):
            return True

    return j == (len(list_b) - 1)


def main():
    """
    Main.
    """
    list_a = [1, 2, 3, 4, 5, 6, 7, 8]
    list_b = [5, 6, 7, 8, 1, 2, 3, 4]
    print(is_rotated_list(list_a, list_b))


if __name__ == '__main__':
   sys.exit(main())
