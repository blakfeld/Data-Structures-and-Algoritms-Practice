#!/usr/bin/env python
"""
most_frequent_int.py:
    Find the most frequent integer in an list_to_search

Author: Corwin Brown <blakfeld@gmail.com>
"""
from __future__ import print_function

import sys
from collections import defaultdict

import utils


def find_most_frequent_int(list_to_search):
    """
    Find the item that occurs most frequently.

    Args:
        list_to_search (list):   The list to search.

    Returns:
        int
    """
    count = defaultdict(int)
    for item in list_to_search:
        count[item] += 1

    return max(count, key=count.get)


def main():
    """
    Main.
    """
    list_to_search = utils.get_random_list(length=100)
    print(list_to_search)
    print(find_most_frequent_int(list_to_search))

if __name__ == '__main__':
   sys.exit(main())
