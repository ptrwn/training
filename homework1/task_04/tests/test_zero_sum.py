from typing import List

import pytest

from homework1.task_04.zero_sum.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["lists", "expected_result"],
    [
        ([[1, 100], [-1, 100], [1, 100], [-1, 100]], 1),
        ([[1, 100], [1, 100], [1, 100], [1, 100]], 0),
    ],
)
def test_zero_sum(lists: List, expected_result: int):
    actual_result = check_sum_of_four(*lists)

    assert actual_result == expected_result
