#!/usr/bin/env python
"""
https://www.hackerrank.com/challenges/anagram
"""
import sys
from collections import defaultdict


def diff_anagram(word_one, word_two):
    """
    Count the number of differing characters in word_one and two

    Args:
        word_one (str):     The first word to check...
        word_two (str):     ... and the second.

    Returns:
        int -- How many characters to change to get an anagram.
    """
    counter = defaultdict(int)
    for char in word_one:
        counter[char] += 1

    for char in word_two:
        counter[char] -= 1

    return sum(filter(lambda x: x > 0, counter.values()))


def split_word(word):
    """
    Evenly split one string into two equal strings.

    Args:
        word (str): String to split.

    returns:
        Tuple -- (word_one, word_two)
    """
    size = len(word) / 2

    return word[:size], word[size:]


def parse_input():
    """
    Parse command line input.

    First input will be the number of arguments, the rest will be
        the arguments themselves.

    Returns:
        list of arguments.
    """

    args = []
    num_args = int(raw_input())
    for i in xrange(0, num_args):
        args.append(raw_input())

    return args


def main():
    """
    Main
    """
    args = parse_input()
    for arg in args:
        if len(arg) % 2 != 0:
            print(-1)
        else:
            word_one, word_two = split_word(arg)
            print(diff_anagram(word_one, word_two))


if __name__ == '__main__':
    sys.exit(main())
