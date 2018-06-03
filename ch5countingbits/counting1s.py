#!/usr/bin/env python

import time

def naive(value):
    count = 0
    while (value):
        count += 1 if (value & 1) else 0
        value = value >> 1
    return count


def divide_conquer(value):
    value = (value & 0x55555555) + ((value >> 1) & 0x55555555)
    value = (value & 0x33333333) + ((value >> 2) & 0x33333333)
    value = (value & 0x0F0F0F0F) + ((value >> 4) & 0x0F0F0F0F)
    value = (value & 0x00FF00FF) + ((value >> 8) & 0x00FF00FF)
    value = (value & 0x0000FFFF) + ((value >> 16) & 0x0000FFFF)
    return value


def pop(value):
    """
    based on equation:

    num_1_bits = x - x/2 - x/4 - ... - x/2^31
    """
    value = value - ((value >> 1) & 0x55555555)
    value = (value & 0x33333333) + ((value >> 2) & 0x33333333)
    value = (value + (value >> 4)) & 0x0F0F0F0F
    value = value + (value >> 8)
    value = value + (value >> 16)
    return value & 0x0000003F


def hakmem(x):
    n = (x >> 1) & 0o333333333333
    x = x - n
    n = (n >> 1) & 0o333333333333
    x = x - n
    x = (x + (x >> 3)) & 0o30707070707
    return x % 63


def test_suite(f, iterations, value, expected,  title=None):
    if not title:
        title = f.__name__ if '__name__' in dir(f) else str(f)
    assert expected == f(value)
    start = time.time()
    for i in range(iterations):
        f(i)
    print('{} ({}):'.format(title, iterations), time.time() - start)


if __name__ == '__main__':
    test_suite(naive, 100000, 0b1000101110110, 7)
    test_suite(divide_conquer, 100000, 0b1000101110110, 7)
    test_suite(pop, 100000, 0b1000101110110, 7)
    test_suite(hakmem, 100000, 0b1000101110110, 7)

