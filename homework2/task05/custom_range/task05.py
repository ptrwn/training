"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""

from typing import Any, Iterable, List


def custom_range(iter: Iterable[Any], required, *args) -> List[Any]:

    if not args:
        stop = required
        return list(iter[: iter.index(stop)])
    elif len(args) == 1:
        start = required
        stop = args[0]
        return list(iter[iter.index(start) : iter.index(stop)])
    elif len(args) == 2:
        start = required
        stop = args[0]
        step = args[1]

        if not isinstance(step, int):
            raise ValueError("Step can be only of integer type.")

        return list(iter[iter.index(start) : iter.index(stop) : step])

    else:
        raise ValueError("3 arguments most are accepted.")
