#!/usr/bin/env python
"""
lru_cache.py:
    Implementation of an LRU cache.
"""
from __future__ import absolute_import, print_function

import sys


class Node(object):
    next = None
    prev = None

    def __init__(self, data):
        self.data = data


class Cache(object):
    """
    {
        'key': {
            'value': 'value'
            'node': <node_obj>
        }
    }
    """
    def __init__(self, max_size=10):
        """
        Constructor.
        """
        self._cache = {}
        self._head = Node('head')
        self._last = Node('last')
        self._max_size = max_size

        self._head.next = self._last
        self._last.prev = self._head

    def get(self, key):
        value = None
        if key in self._cache:
            value = self._cache[key]['value']
            self.insert(key, value)

        return value

    def insert(self, key, value):
        if key in self._cache:
            node = self._unlink_node(self._cache[key]['node'])
        else:
            node = Node(key)

        self._insert_first(node)
        self._cache[key] = {'value': value, 'node': node}

        self._evict()

    def _insert_first(self, node):
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node
        self._head.next = node

    def _evict(self):
        if len(self._cache.keys()) >= self._max_size:
            last = self._unlink_node(self._last.prev)
            key = last.data
            del self._cache[key]

    def _unlink_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

        return node


def print_linked_list(ll):
    result = []
    while ll:
        result.append(ll.data)
        ll = ll.next

    return ' -> '.join(result)


def main():
    """
    Main.
    """
    cache = Cache()

    cache.insert('one', 'one')
    cache.insert('two', 'two')
    cache.insert('three', 'three')
    cache.insert('four', 'four')
    cache.insert('five', 'five')
    cache.get('one')
    cache.insert('six', 'six')
    cache.insert('seven', 'seven')
    cache.insert('eight', 'eight')
    cache.insert('nine', 'nine')
    cache.insert('ten', 'ten')
    cache.insert('eleven', 'eleven')
    cache.insert('twelve', 'twelve')
    cache.insert('thirteen', 'thirteen')


if __name__ == '__main__':
    sys.exit(main())
