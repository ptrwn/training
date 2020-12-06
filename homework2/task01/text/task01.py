"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols +
    2) Find rarest symbol for document + 
    3) Count every punctuation char +
    4) Count every non ascii char +
    5) Find most common non ascii char for document +
"""
import string
from typing import Dict, List


def prepare_text(file_path: str) -> List[str]:
    """Read contents of file, replace unicode chars."""

    with open(file_path, "r") as f:
        lines = f.readlines()

    # replace '\u00e4' representations with the actual symbols:
    res = [part.encode("latin1").decode("unicode_escape") for part in lines]

    return res


def merge_wrapped_words(words_list: List[str]) -> List[str]:
    """Merge words separateld by line wraps (or breaks)."""

    words_without_wraps = []

    skip_next = False
    for num, word in enumerate(words_list):
        if skip_next:
            skip_next = False
            continue

        if word.endswith("-"):
            first_word_part = word.rstrip("-")
            second_word_part = words_list[num + 1]
            words_without_wraps.append(first_word_part + second_word_part)
            skip_next = True
        else:
            words_without_wraps.append(word)

    return words_without_wraps


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Find 10 longest words consisting from largest amount of unique symbol."""

    # punctuation_extended is '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~»«—'
    # .replace('-', '') -- need to keep '-' symbol because it marks
    # parts of words broken by line wrap, will be used later to merge
    punctuation_extended = string.punctuation.replace("-", "") + "»«—"

    res = prepare_text(file_path)

    # remove tabs, newlines, and punctuation, put all words in one list
    words_list = [
        word.strip(punctuation_extended)
        for line in res
        for word in line.strip("\t\n").split(" ")
        if word
    ]

    # merge parts of words separated by wrap (as in 'erschaf-' + 'fene')
    words_without_wraps = merge_wrapped_words(words_list)

    # remove duplicates
    unique_words = list(set(words_without_wraps))

    # make a dict where each unique word keys sum of its length with number of
    # its unique symbols - so that we get max in both criteria
    counter = {word: len(word) + len(set(word)) for word in unique_words}

    # sort by length, take ten longest
    longest_diverse = [
        item[0]
        for item in list(
            sorted(counter.items(), key=lambda item: item[1], reverse=True)
        )[:10]
    ]

    return longest_diverse


def get_rarest_char(file_path: str) -> str:
    """ Find rarest symbol for document."""

    res = prepare_text(file_path)

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

    punctuation_extended = string.punctuation + "»«—"

    res = prepare_text(file_path)

    # remove tabs and newlines, put all words in one list
    words_list = [
        word for line in res for word in line.strip("\t\n").split(" ") if word
    ]

    w_srt = "".join(words_list)

    counter = {}

    for i in w_srt:
        if i in punctuation_extended:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

    return counter


def count_non_ascii_chars(file_path: str) -> Dict[str, int]:
    """ Count every non ascii char."""

    res = prepare_text(file_path)

    counter = {}

    for line in res:
        for word in line.strip("\t\n"):
            for sym in word:
                if not sym.isascii():
                    if sym in counter:
                        counter[sym] += 1
                    else:
                        counter[sym] = 1

    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Find most common non ascii char for document."""

    counter = count_non_ascii_chars(file_path)

    # get a list of tuples sorted by symbol occurrence from largest to smallest
    sort_count = [
        item
        for item in list(
            sorted(counter.items(), key=lambda item: item[1], reverse=True)
        )
    ]

    return sort_count[0][0]
