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

def locate_seed(srange: tuple[int, int], maps: list[Map], cache: dict[tuple[int, int], int]) -> int:
    minimum = sys.maxsize
    for location_src in range(srange[0], srange[0] + srange[1] + 1):
        location_dst = location_src
        for imap, amap in enumerate(maps):
            if (imap, location_src) not in cache:
                for dst, src, length in amap:
                    if src <= location_src <= src + length:
                        location_dst = dst + (location_src - src)
                        break
                cache[(imap, location_src)] = location_dst
            location_dst = cache[(imap, location_src)]
        minimum = min(location_dst, minimum)

    return minimum

# Main Execution

def main(stream=sys.stdin) -> None:
    seeds, maps = read_almanac(stream)
    cache       = {}
    locations   = [locate_seed(srange, maps, cache) for srange in batched(seeds, 2)]
    print(min(locations))

if __name__ == '__main__':
    main()
