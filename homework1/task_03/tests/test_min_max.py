import pytest

from homework1.task_03.min_max.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("homework1/task_03/min_max/in.txt", (-1, 1000)),
    ],
)
def test_min_max(file_name: str, expected_result: bool):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
