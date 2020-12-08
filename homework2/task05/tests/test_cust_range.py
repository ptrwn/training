import string
from typing import Any, Iterable, List

import pytest

from homework2.task05.custom_range.task05 import custom_range


@pytest.mark.parametrize(
    ["inp", "expected_result"],
    [
        (([1, 2, 3, 4, 5, 6], 4), [1, 2, 3]),
        ((string.ascii_lowercase, "g"), ["a", "b", "c", "d", "e", "f"]),
        (([1, 2, 3, 4, 5, 6], 2, 6), [2, 3, 4, 5]),
        (
            (string.ascii_lowercase, "g", "p"),
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        (([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 1, -1), [4, 3, 2]),
        ((string.ascii_lowercase, "p", "g", -2), ["p", "n", "l", "j", "h"]),
    ],
)
def test_custom_range(inp: Iterable[Any], expected_result: List[Any]):

    actual_result = custom_range(*inp)

    assert actual_result == expected_result
