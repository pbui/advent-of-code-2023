#!/usr/bin/env python3

''' Day 04 - Part A '''

from typing import Iterator
import re
import sys

# Types

Numbers = set[int]
Card    = list[Numbers, Numbers]

# Functions

def read_cards(stream=sys.stdin) -> Iterator[Card]:
    for line in stream:
        yield [set(map(int, n.split())) for n in line.split(':')[-1].split('|')]

# Main Execution

def main(stream=sys.stdin) -> None:
    cards  = [numbers & winning for winning, numbers in read_cards(stream)]
    points = sum(2**(len(card)-1) for card in cards if card)
    print(points)

if __name__ == '__main__':
    main()
