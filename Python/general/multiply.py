#!/usr/bin/env python
"""
multiply.py:
    Write a multiply function that multiples 2 integers without
    using *.

Author: Corwin Brown <corwin@corwinbrown.com>
"""
from __future__ import print_function, absolute_import

import sys


def multiply(left, right):
    """
    """
    return sum([left for _ in xrange(right)])


def main():
    """
    Main.
    """
    print(multiply(5, 12))


if __name__ == '__main__':
    sys.exit(main())
