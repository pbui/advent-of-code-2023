#!/usr/bin/env python3

''' Day 04 - Part B '''

from collections import defaultdict
from typing      import Iterator

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
    counts = defaultdict(int)

    for index, card in enumerate(cards, 1):
        counts[index] += 1
        for copy in range(index + 1, index + len(card) + 1):
            counts[copy] += counts[index]

    print(sum(counts.values()))

if __name__ == '__main__':
    main()
