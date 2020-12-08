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
from collections.abc import Callable


def cacher(func: Callable) -> Callable:
    cache = dict()

    def cached_func(*args):
        if args in cache:
            return cache[args]
        res = func(*args)
        cache[args] = res
        return res

    return cached_func
