#!/usr/bin/env python
"""
int_to_binary.py

Author: Corwin Brown <blakfeld@gmail.com>
"""
from __future__ import print_function

import sys


def convert_int_to_binary(int_to_convert):
    """
    Convert an int to binary.
    
    I'm aware that in python I could've just done:
        '{0:b}'.format(int_to_convert)
    But that's a little less informative :)

    Args:
        int_to_convert (int):   The int to convert.

    Returns:
        str
    """
    result = []
    while int_to_convert != 0:
        result.append(int_to_convert % 2)
        int_to_convert = int_to_convert // 2

    return ''.join([str(b) for b in result[::-1]])


def main():
    """
    Main.
    """
    print(convert_int_to_binary(156))


if __name__ == '__main__':
   sys.exit(main())
