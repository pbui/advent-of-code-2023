#!/usr/bin/env python3

''' Day 01 - Part B '''

import sys

# Constants

DIGITS = (
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
)

# Functions

def word_to_digit(s: str, index: int) -> str:
    for value, digit in enumerate(DIGITS, 1):
        if s[index:].startswith(digit):
            return str(value)
    return s[index]

def read_values(stream=sys.stdin) -> list[list[str]]:
    return [
        list(filter(str.isdigit, map(lambda p: word_to_digit(line, p[0]), enumerate(line))))
        for line in stream
    ]

# Main Execution

def main(stream=sys.stdin) -> None:
    values = read_values(stream)
    total  = sum(
        int(digits[0] + digits[-1]) for digits in values
    )
    print(total)

if __name__ == '__main__':
    main()
