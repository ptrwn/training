from typing import Any, List

import pytest

from homework2.task03.combinations.task03 import combinations


@pytest.mark.parametrize(
    ["inp", "expected_result"],
    [
        (
            [[1, 2, 3], ["a", "b"]],
            [[1, "a"], [1, "b"], [2, "a"], [2, "b"], [3, "a"], [3, "b"]],
        ),
    ],
)
def test_combinations(inp: List[Any], expected_result: List[List]):

    actual_result = combinations(*inp)

    assert actual_result == expected_result
