from pathlib import Path
from typing import Dict, List

import pytest

from homework2.task01.text.task01 import (
    count_punctuation_chars,
    get_longest_diverse_words,
    get_rarest_char,
)

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


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [(file_path, "W—IyTLAPGzBjpq")],
)
def test_get_rarest_char(file_path: str, expected_result: str):

    actual_result = get_rarest_char(file_path)

    assert actual_result in expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [(file_path, {"—": 1, ",": 3, ".": 2, "-": 2})],
)
def test_count_punctuation_chars(file_path: str, expected_result: Dict[str, int]):

    actual_result = count_punctuation_chars(file_path)

    assert actual_result == expected_result
