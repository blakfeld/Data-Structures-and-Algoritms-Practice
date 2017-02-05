#!/usr/bin/env python
"""
exponent.py

Author: Corwin Brown <corwin@corwinbrown.com>
"""
from __future__ import print_function, absolute_import

import sys


def exponent(base, power):
    """
    """
    result = base
    for i in xrange(1, power):
        result *= base

    return result


def main():
    """
    Main.
    """
    print(exponent(4, 2))


if __name__ == '__main__':
    sys.exit(main())
