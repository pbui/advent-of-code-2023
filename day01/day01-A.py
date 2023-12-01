#!/usr/bin/env python3

''' Day 01 - Part A '''

import sys

# Functions

def read_values(stream=sys.stdin) -> list[list[str]]:
    return [
        list(filter(str.isdigit, line))
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
