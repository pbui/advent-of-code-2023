#!/usr/bin/env python3

''' Day 03 - Part A '''

from typing import Iterator
import re
import sys

# Types

Schematic = list[str]
Number    = tuple[int, int, int]

# Constants

DIRECTIONS = (
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1),
)

# Functions

def read_schematic(stream=sys.stdin) -> Schematic:
    schematic = [line.strip() for line in stream]
    columns   = len(schematic[0]) + 2
    return [
        '.'*columns,
        *['.' + line + '.' for line in schematic],
        '.'*columns,
    ]

def is_symbol(s: str) -> bool:
    return not (s.isdigit() or s == '.')

def find_numbers(schematic: Schematic) -> Iterator[Number]:
    rows    = len(schematic)
    columns = len(schematic[0])

    for r in range(1, rows):
        for number in re.finditer(r'[0-9]+', schematic[r]):
            yield (r, *number.span())

def find_parts(schematic: Schematic, numbers: Iterator[Number]) -> Iterator[int]:
    for r, c_head, c_tail in numbers:
        part = int(schematic[r][c_head:c_tail])
        for c in range(c_head, c_tail):
            neighbors = (schematic[r + dr][c + dc] for dr, dc in DIRECTIONS)
            if any(is_symbol(neighbor) for neighbor in neighbors):
                yield part
                break

# Main Execution

def main(stream=sys.stdin) -> None:
    schematic = read_schematic(stream)
    numbers   = find_numbers(schematic)
    parts     = find_parts(schematic, numbers)
    print(sum(parts))

if __name__ == '__main__':
    main()
