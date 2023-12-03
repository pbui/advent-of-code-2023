#!/usr/bin/env python3

''' Day 03 - Part B '''

from typing import Iterator
import re
import sys

# Types

Schematic = list[str]
Number    = tuple[int, int, int]
Star      = tuple[int, int]

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

def find_stars(schematic: Schematic) -> Iterator[Star]:
    rows    = len(schematic)
    columns = len(schematic[0])

    for r in range(1, rows):
        for c in range(1, columns):
            token = schematic[r][c]
            if token == '*':
                yield (r, c)

def find_gears(schematic: Schematic, stars: Iterator[Star], numbers: list[Number]) -> Iterator[int]:
    for star_r, star_c in stars:
        gears = [
            int(schematic[number_r][number_c_head:number_c_tail])
            for number_r, number_c_head, number_c_tail in numbers
            if any(star_r + dr == number_r and number_c_head <= (star_c + dc) < number_c_tail for dr, dc in DIRECTIONS)
        ]
        if len(gears) == 2:
            yield gears[0] * gears[1]

# Main Execution

def main(stream=sys.stdin) -> None:
    schematic = read_schematic(stream)
    numbers   = find_numbers(schematic)
    stars     = find_stars(schematic)
    gears     = find_gears(schematic, stars, list(numbers))
    print(sum(gears))

if __name__ == '__main__':
    main()
