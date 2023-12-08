#!/usr/bin/env python3

''' Day 08 - Part A '''

from collections import defaultdict
from typing      import Iterator

import itertools
import sys
import re

# Types

Network = dict[str, dict[str, str]]

# Functions

def read_instructions(stream=sys.stdin) -> Iterator[str]:
    return itertools.cycle(stream.readline().strip())

def read_network(stream=sys.stdin) -> Network:
    network = defaultdict(dict)

    for line in map(str.strip, stream):
        if not line:
            continue

        source, target_l, target_r = re.findall('[A-Z]{3}', line)
        network[source] = {
            'L': target_l,
            'R': target_r,
        }

    return network

def navigate(instructions: Iterator[str], network: Network) -> int:
    count  = 0
    source = 'AAA'
    target = 'ZZZ'

    while source != target:
        source = network[source][next(instructions)]
        count += 1

    return count

# Main Execution

def main(stream=sys.stdin) -> None:
    instructions = read_instructions(stream)
    network      = read_network(stream)
    print(navigate(instructions, network))

if __name__ == '__main__':
    main()
