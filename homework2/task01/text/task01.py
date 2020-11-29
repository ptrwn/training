"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols +
    2) Find rarest symbol for document + 
    3) Count every punctuation char +
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import Dict, List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from largest amount of unique symbol."""

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

    # remove duplicates
    unique_words = list(set(clean_words))

    # make a dict where each unique word keys sum of its length with number of
    # its unique symbols - so that we get max in both criteria
    counter = {word: len(word) + len(set(word)) for word in unique_words}

    # sort by length, take ten longest
    longest_diverse = [
        item[0]
        for item in list(sorted(counter.items(), key=lambda item: item[1]))[-10:]
    ]

    return longest_diverse


def get_rarest_char(file_path: str) -> str:
    """ Find rarest symbol for document."""

    with open(file_path, "r") as f:
        lines = f.readlines()

    # replace '\u00e4' representations with the actual symbols:
    res = [part.encode("latin1").decode("unicode_escape") for part in lines]

    # remove tabs and newlines, put all words in one list
    words_list = [
        word for line in res for word in line.strip("\t\n").split(" ") if word
    ]

    w_str = "".join(words_list)

    counter = {}

    for i in w_str:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    # get a list of tuples sorted by symbol occurrence from smalles to largest
    sort_count = [
        item for item in list(sorted(counter.items(), key=lambda item: item[1]))
    ]

    return sort_count[0][0]


def count_punctuation_chars(file_path: str) -> Dict[str, int]:
    """Count every punctuation char."""

    with open(file_path, "r") as f:
        lines = f.readlines()

    # replace '\u00e4' representations with the actual symbols:
    res = [part.encode("latin1").decode("unicode_escape") for part in lines]

    # remove tabs and newlines, put all words in one list
    words_list = [
        word for line in res for word in line.strip("\t\n").split(" ") if word
    ]

    w_srt = "".join(words_list)

    counter = {}

    for i in w_srt:
        if i in "».,()?!-«—'\"":
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

    return counter


def count_non_ascii_chars(file_path: str) -> Dict[str, int]:
    """ Count every non ascii char."""

    with open(file_path, "r") as f:
        lines = f.readlines()

    # replace '\u00e4' representations with the actual symbols:
    res = [part.encode("latin1").decode("unicode_escape") for part in lines]

    # remove tabs and newlines, put all words in one list
    words_list = [
        word for line in res for word in line.strip("\t\n").split(" ") if word
    ]

    w_srt = "".join(words_list)

    counter = {}

    for i in w_srt:
        if ord(i) > 127:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...
