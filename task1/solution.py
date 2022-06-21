#! /usr/bin/env python3
"""
PlusMinusConversion
Write a function solution that, given a string S of length N, replaces all
occurrences of "plus" with "+" and all occurrences of "minus" with "-".
"""


def solution(S: str) -> str:
    """
    TODO: insert pydoc here
    """
    res = S.lower()
    res = res.replace(r"plus", "+")
    res = res.replace(r"minus", "-")
    return res


if __name__ == "__main__":
    S = "minusplusminus"
    print(solution(S))
    S = "plusminusminusplus"
    print(solution(S))
