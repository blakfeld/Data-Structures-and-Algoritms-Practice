#!/usr/bin/env python
"""
stack_list.py:
    Python implementation of a stack, using a list.
"""
from __future__ import absolute_import, print_function

import sys

class StackList(object):
    """
    First-In Last-Out Data Structure.
    """

    def __init__(self):
        """
        Constructor.
        """
        self._stack = []
        self._length = -1

    def is_empty(self):
        """
        Check if stack is empty.
        """
        return self._length == -1

    def pop(self):
        """
        Pop Stack Operation.
        """
        result = self._stack[self._length]
        self._length -= 1

        return result

    def push(self, value):
        """
        Push Stack Operation.

        Args:
            value (?):  Value to push onto stack.
        """
        self._length += 1
        self._stack.append(value)


def main():
    """
    Main.
    """
    stack = StackList()

    stack.push(1)
    stack.push(4)
    stack.push(10)
    stack.push(5)

    result = []
    while not stack.is_empty():
        result.append(stack.pop())

    print(result)
    assert result == [5, 10, 4, 1]



if __name__ == '__main__':
    sys.exit(main())
