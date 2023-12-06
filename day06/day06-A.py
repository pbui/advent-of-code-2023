#!/usr/bin/env python3

''' Day 06 - Part A '''

import sys

# Functions

def race(charge_time: int, total_time: int) -> int:
    return charge_time * (total_time - charge_time)

# Main Execution

def main(stream=sys.stdin) -> None:
    times     = [int(t) for t in stream.readline().split(':')[-1].split()]
    distances = [int(d) for d in stream.readline().split(':')[-1].split()]
    product   = 1

    for time, distance in zip(times, distances):
        ways     = [c for c in range(1, time + 1) if race(c, time) > distance]
        product *= len(ways)

    print(product)

if __name__ == '__main__':
    main()
