from typing import Tuple

import pytest

from homework1.task_05.max_subarr.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["args", "expected_result"],
    [
        (([1, 3, -1, -3, 5, 3, 6, 7, 10], 3), 23),
        (([-1, -1, -1, 100, -1, -1], 3), 100),
    ],
)
def test_max_subarr(args: Tuple, expected_result: int):
    actual_result = find_maximal_subarray_sum(*args)

    assert actual_result == expected_result
