#!/usr/bin/env python3

''' Day 05 - Part A '''

from collections import deque
from typing      import Iterator

import concurrent.futures
import functools
import itertools
import re
import sys

# Types

Seeds = list[int]
Range = tuple[int, int]
Map   = tuple[int, int, int]
Maps  = list[Map]

# Functions

def batched(iterable, n):
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(itertools.islice(it, n)):
        yield batch

def read_almanac(stream=sys.stdin) -> tuple[Seeds, Maps]:
    seeds: Seeds = [int(seed) for seed in stream.readline().split(':')[-1].split()]
    maps:  Maps  = []

    for line in map(str.strip, stream):
        if line.endswith('map:'):
            maps.append([])
            continue

        try:
            dst, src, length = map(int, line.split())
        except ValueError:
            continue

        maps[-1].append((dst, src, length))

    return seeds, maps

def locate_seed(seed: int, maps: Maps={}) -> int:
    location = seed
    for amap in maps:
        for dst, src, length in amap:
            if src <= location < src + length:
                location = dst + (location - src)
                break
    return location

def locate_seeds(srange: Range, maps: Maps={}) -> int:
    seeds   = range(srange[0], srange[0] + srange[1])
    locator = functools.partial(locate_seed, maps=maps)
    return min(map(locator, seeds))

# Main Execution

def main(stream=sys.stdin) -> None:
    seeds, maps = read_almanac(stream)
    locator     = functools.partial(locate_seeds, maps=maps)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        locations = executor.map(locator, batched(seeds, 2))

    print(min(locations))

if __name__ == '__main__':
    main()
