#!/usr/bin/env python
"""
Take two user supplied strings, and determine whether or not they are
    anagrams of each other.

Usage:
    anagrams.py <word_one> <word_two> [--use-sorting]

Options:
    --use-sorting     Use the sorting algorithm.
"""
import sys
from collections import defaultdict

import docopt


class Anagram(object):
    def __init__(self, use_sorting=False):
        """
        Constructor.

        Args:
            use_sorting (bool): If true, use the sorting algoritm, otherwise
                                    use hashing/counting.
        """
        self.use_sorting = use_sorting

    def is_anagram(self, word_one, word_two):
        """
        Determine if the two words are anagrams.

        Args:
            word_one (str):     A word to test.
            word_two (str):     The second word to test.

        Returns:
            bool
        """
        if self.use_sorting:
            return self._sorting_algo(word_one, word_two)
        else:
            return self._counting_algo(word_one, word_two)

    def _sorting_algo(self, word_one, word_two):
        """
        Use the sorting algorithm to determine if two words are anagrams.

        Args:
            word_one (str):     A word to test.
            word_two (str):     The second word to test.

        Returns:
            bool
        """

        return sorted(word_one) == sorted(word_two)

    def _counting_algo(self, word_one, word_two):
        """
        Use the counting algoritm to determine if two words are anagrams.

        Args:
            word_one (str):     A word to test.
            word_two (str):     The second word to test.

        Returns:
            bool
        """
        if len(word_one) != len(word_two):
            return False

        counter = defaultdict(int)
        for char in word_one:
            counter[char] += 1

        for char in word_two:
            counter[char] -= 1
            if counter[char] < 0:
                return False

        return True


def parse_args():
    """
    Parse command line arguments.

    Returns:
        dict
    """
    return docopt.docopt(__doc__)


def main(args):
    """
    Main
    """

    word_one = args['<word_one>']
    word_two = args['<word_two>']
    use_sorting = args['--use-sorting']

    anagram = Anagram(use_sorting=use_sorting)
    print(anagram.is_anagram(word_one, word_two))

    return 0

if __name__ == '__main__':
    sys.exit(main(parse_args()))
