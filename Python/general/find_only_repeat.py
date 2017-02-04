#!/usr/bin/env python
"""
find_only_repeat.py
    Find the only element in an array that only occurs once.

Author: Corwin Brown <blakfeld@gmail.com>
"""
from __future__ import print_function

import sys
from collections import defaultdict


def find_only_repeat(list_to_search):
    """
    Search a list for a single repeating int.

    Args:
        list_to_search (list):  The list to search.

    Returns:
        int
    """
    count = defaultdict(int)
    for item in list_to_search:
        count[item] += 1

    return min(count, key=count.get)


def main():
    """
    Main.
    """
    list_to_search = [0, 1, 5, 0, 1, 8, 7, 8, 7]
    print(find_only_repeat(list_to_search))


if __name__ == '__main__':
   sys.exit(main())
