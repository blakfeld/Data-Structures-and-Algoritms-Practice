#!/usr/bin/env python
"""
queue_list.py:
    Python implementation of a Queue, using a list.
"""
from __future__ import absolute_import, print_function

import sys


class QueueList(object):
    """
    First In First Out Data Structure.
    """

    def __init__(self):
        """
        Constructor.
        """
        self._queue = []

    def is_empty(self):
        """
        Check if Queue is empty.
        """
        return len(self._queue) == 0

    def pop(self):
        """
        Pop a value out of the queue.
        """
        if not self.is_empty():
            return self._queue.pop(0)

    def push(self, value):
        """
        Push a value into the queue.

        Args:
            value (?):  Value to push onto the stack.
        """
        self._queue.append(value)


def main():
    """
    Main.
    """
    queue = QueueList()

    queue.push(0)
    queue.push(5)
    queue.push(4)
    queue.push(100)
    queue.push(30)

    result = []
    while not queue.is_empty():
        result.append(queue.pop())

    print(result)
    assert result == [0, 5, 4, 100, 30]


if __name__ == '__main__':
    sys.exit(main())
