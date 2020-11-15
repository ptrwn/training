"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which accepts a Sequence
of integers, and returns if the given sequence is a Fibonacci
sequence.
We guarantee, that the given sequence contain >= 0 integers inside.
UPD.:
- should be True for [0], [0, 1], [0, 1, 1]
- ONLY Fib nums, should be False for [1, 100, 101, 201, 302, ...]
"""

from typing import List


def fib(n: int):
    a, b, counter = 0, 1, 1
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


def check_fibonacci(data: List[int]) -> bool:
    if len(data) == 0:
        return False
    else:
        return data == list(fib(len(data)))
