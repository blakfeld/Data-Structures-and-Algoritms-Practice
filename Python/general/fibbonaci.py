#!/usr/bin/env python
"""
fibbonaci.py
    Write fibbonaci iteratively and recursively
    (bonus: use dynamic programming).

    1, 1, 2, 3, 5, 8, 13, 21, 34 ...

Author: Corwin Brown <blakfeld@gmail.com>
"""
from __future__ import print_function

import sys


LIMIT = 10


def fibbonaci_recursive(i=0, j=1, count=0):
    """
    A recursive implementation of a fibbonaci sequence generator.

    Args:
        i (int):        The number to start the sequence with.
        j (int):        The second number in the sequence.
        count (int):    How many numbers are in our sequence.
    """
    if count == LIMIT:
        return

    print(i)
    fibbonaci_recursive(j, j + i, count + 1)


def fibbonaci_iterative():
    """
    An interative implementation of a fibbonaci sequence generator.
    """
    i, j = (0, 1)
    for _ in xrange(LIMIT):
        print(i)
        tmp = i
        i = j
        j += tmp


def fibbonaci_dynamic():
    """
    """
    pass


def main():
    """
    Main.
    """
    print('Recursive:')
    fibbonaci_recursive()
    
    print('\nIterative:')
    fibbonaci_iterative()
    pass


if __name__ == '__main__':
   sys.exit(main())
