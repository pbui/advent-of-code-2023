#!/usr/bin/env python3

''' Day 08 - Part B '''

from collections import defaultdict
from itertools   import cycle
from typing      import Iterator

import math
import sys
import re

# Types

Network = dict[str, dict[str, str]]

# Functions

def read_instructions(stream=sys.stdin) -> Iterator[str]:
    return stream.readline().strip()

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

def navigate(instructions: Iterator[str], network: Network, element: str) -> int:
    count = 0

    while not element.endswith('Z'):
        element = network[element][next(instructions)]
        count += 1

    return count

def locate_ghosts(network: Network) -> list[str]:
    return [element for element in network if element.endswith('A')]

# Main Execution

def main(stream=sys.stdin) -> None:
    instructions = read_instructions(stream)
    network      = read_network(stream)
    ghosts       = locate_ghosts(network)
    counts       = [navigate(cycle(instructions), network, ghost) for ghost in ghosts]
    print(math.lcm(*counts))

if __name__ == '__main__':
    main()
