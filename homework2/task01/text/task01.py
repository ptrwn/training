"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:

    with open(file_path, "r") as f:
        lines = f.readlines()

    # replace '\u00e4' representations with the actual symbols:
    res = [part.encode("latin1").decode("unicode_escape") for part in lines]

    # remove tabs, newlines, and punctuation, put all words in one list
    words_list = [
        word.strip("».,()«—")
        for line in res
        for word in line.strip("\t\n").split(" ")
        if word
    ]

    # merge parts of words separated by wrap (as in 'erschaf-' + 'fene')
    clean_words = []
    for num, el in enumerate(words_list):

        if el and el.endswith("-"):
            clean_words.append(el[:-1] + words_list[num + 1])
        elif el and words_list[num - 1].endswith("-"):
            continue
        else:
            el and clean_words.append(el)

    print(clean_words)


get_longest_diverse_words("data.txt")


def get_rarest_char(file_path: str) -> str:
    ...


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...
