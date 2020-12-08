from typing import Any, List

import pytest

from homework2.task04.cache.task04 import cacher


def func(a, b):
    return (a ** b) ** 2


cache_func = cacher(func)


def test_cache():

    some = 1, 2
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


def test_cache_kw():

    val_1 = cache_func(a=2, b=3)
    val_2 = cache_func(a=2, b=3)
    assert val_1 is val_2
