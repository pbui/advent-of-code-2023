#!/usr/bin/env python3

''' Day 05 - Part A '''

from typing import Iterator
import itertools
import re
import sys

# Types

Seeds = list[int]
Map   = tuple[int, int, int]
Maps  = list[Map]

# Functions

def batched(iterable, n):
	if n < 1:
		raise ValueError('n must be at least one')
	it = iter(iterable)
	while batch := tuple(itertools.islice(it, n)):
		yield batch

def read_almanac(stream=sys.stdin) -> tuple[Seeds, list[Map]]:
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

def locate_seed(srange: tuple[int, int], maps: list[Map]) -> int:
    minimum = sys.maxsize
    for location in range(srange[0], srange[0] + srange[1] + 1):
        for amap in maps:
            for dst, src, length in amap:
                if src <= location <= src + length:
                    location = dst + (location - src)
                    break
        minimum = min(location, minimum)

    return minimum

# Main Execution

def main(stream=sys.stdin) -> None:
    seeds, maps = read_almanac(stream)
    locations   = [locate_seed(srange, maps) for srange in batched(seeds, 2)]
    print(min(locations))

if __name__ == '__main__':
    main()
