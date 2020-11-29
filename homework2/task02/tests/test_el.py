from typing import List, Tuple

import pytest

from homework2.task02.most_least_common_el.task02 import major_and_minor_elem


@pytest.mark.parametrize(
    ["inp", "expected_result"],
    [
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        ([3, 2, 3], (3, 2)),
        ([3, 3, 3, 3, 3, 3, 3], (3, 3)),
    ],
)
def test_major_and_minor_elem(inp: List[int], expected_result: Tuple[int, int]):

    actual_result = major_and_minor_elem(inp)

    assert actual_result == expected_result
