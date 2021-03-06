from typing import List

import pytest

from homework1.task_02.fib.task02 import check_fibonacci


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ([], False),
        ([1], False),
        ([1, 2], False),
        ([1, 1, 1], False),
        ([1, 100, 101, 201, 302], False),
        ([0], True),
        ([0, 1], True),
        ([0, 1, 1], True),
        ([0, 1, 1, 2], True),
    ],
)
def test_fib(data: List[int], expected_result: bool):
    actual_result = check_fibonacci(data)

    assert actual_result == expected_result
