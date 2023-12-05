#!/usr/bin/env python3

''' Day 05 - Part A '''

from typing import Iterator
import re
import sys

# Types

Seeds = list[int]
Map   = tuple[int, int, int]
Maps  = list[Map]

# Functions

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

def locate_seed(seed: int, maps: Maps) -> int:
    location = seed
    for amap in maps:
        for dst, src, length in amap:
            if src <= location < src + length:
                location = dst + (location - src)
                break

    return location

# Main Execution

def main(stream=sys.stdin) -> None:
    seeds, maps = read_almanac(stream)
    locations   = [locate_seed(seed, maps) for seed in seeds]
    print(min(locations))

if __name__ == '__main__':
    main()
