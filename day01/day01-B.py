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

def read_values(stream=sys.stdin) -> list[list[str]]:
    values = []
    for line in stream:
        letters = line.strip()
        digits  = []

        for index, letter in enumerate(letters):
            if letter.isdigit():
                digits.append(letter)

            for value, digit in enumerate(DIGITS, 1):
                if letters[index:].startswith(digit):
                    digits.append(str(value))
                    break

        values.append(digits)
    return values

# Main Execution

def main(stream=sys.stdin) -> None:
    values = read_values(stream)
    print(values)
    total  = sum(
        int(digits[0] + digits[-1]) for digits in values
    )
    print(total)

if __name__ == '__main__':
    main()
