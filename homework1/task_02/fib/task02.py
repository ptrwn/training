"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which accepts a Sequence
of integers, and returns if the given sequence is a Fibonacci
sequence.
We guarantee, that the given sequence contain >= 0 integers inside.
"""

from typing import List


def check_fibonacci(data: List[int]) -> bool:

    if len(data) < 3:
        return False

    a, b, c = data[0], data[1], data[2]

    while len(data) >= 4:

        if not (a + b) == c:
            return False

        data = data[1:]

        a, b, c = b, c, data[2]

    else:
        return (a + b) == c
