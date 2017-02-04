#!/usr/bin/env python
"""
find_first_x_prime_numbers.py:
    Use dynamic programming to find the first X prime numbers.

Author: Corwin Brown <blakfeld@gmail.com>
"""
from __future__ import print_function

import sys


def primes_sieve(limit):
    """
    Find first X prime numbers using the "Sieve of Eratosthenes"
    """
    # Set all numbers in the range as True.
    primes = {i: True for i in xrange(2, limit + 1)}

    # Iterate through all numbers, mark any factors as False, since
    #   they cannot be prime.
    for prime in primes:
        for factor in range(prime, limit + 1, prime)[1:]:
            primes[factor] = False

    return [p for p in primes if primes[p]]


def main():
    """
    Main.
    """
    print(primes_sieve(10000))


if __name__ == '__main__':
   sys.exit(main())
