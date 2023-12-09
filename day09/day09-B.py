#!/usr/bin/env python3

''' Day 09 - Part B '''

import functools
import itertools
import sys

# Functions

def predict(history: list[int]) -> int:
    sequences = [history]
    while len(set(sequences[-1])) > 1:
        sequences.append([b - a for a, b in itertools.pairwise(sequences[-1])])
    return functools.reduce(
        lambda a, b: b - a, [sequence[0] for sequence in reversed(sequences)]
    )

# Main Execution

def main(stream=sys.stdin) -> None:
    histories   = [list(map(int, line.split())) for line in stream]
    predictions = [predict(history) for history in histories]
    print(sum(predictions))

if __name__ == '__main__':
    main()
