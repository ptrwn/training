"""
Write a function that accepts another function as an argument. Then it
should return such a function, that every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from typing import Callable


def cacher(func: Callable) -> Callable:
    cache = dict()

    def cached_func(*args, **kwargs):
        if (args, frozenset(kwargs.items())) in cache:
            return cache[args, frozenset(kwargs.items())]
        res = func(*args, **kwargs)
        cache[args, frozenset(kwargs.items())] = res
        return res

    return cached_func
