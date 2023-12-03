#!/usr/bin/env python3

''' Day 03 - Part A '''

from typing import Iterator
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
        number_head = None
        number_tail = None
        for c in range(1, columns):
            token = schematic[r][c]
            if token.isdigit():
                if not number_head:
                    number_head = c
                number_tail = c
            else:
                if number_head and number_tail:
                    yield (r, number_head, number_tail)
                number_head = None
                number_tail = None

def find_parts(schematic: Schematic, numbers: Iterator[Number]) -> Iterator[int]:
    for r, c_head, c_tail in numbers:
        part = int(schematic[r][c_head:c_tail + 1])
        for c in range(c_head, c_tail + 1):
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
