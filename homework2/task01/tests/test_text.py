from pathlib import Path
from typing import List

import pytest

from homework2.task01.text.task01 import get_longest_diverse_words

file_path = Path(__file__).resolve().parent / "data_short.txt"


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (
            file_path,
            [
                "sondern",
                "Ausflug",
                "Waldgang",
                "vielmehr",
                "verbirgt",
                "Betrachtung",
                "vorgebahnte",
                "bedenklichen",
                "hinausführen",
                "abcdefghijklmnopqrstuvw",
            ],
        )
    ],
)
def test_get_longest_diverse_words(file_path: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(file_path)

    assert set(actual_result) == set(expected_result)
