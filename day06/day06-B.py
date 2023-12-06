#!/usr/bin/env python3

''' Day 06 - Part A '''

import sys

# Functions

def race(charge_time: int, total_time: int):
    return charge_time * (total_time - charge_time)

# Main Execution

def main(stream=sys.stdin) -> None:
    time     = int(''.join(stream.readline().split(':')[-1].split()))
    distance = int(''.join(stream.readline().split(':')[-1].split()))
    ways     = [c for c in range(1, time + 1) if race(c, time) > distance]
    print(len(ways))

if __name__ == '__main__':
    main()
