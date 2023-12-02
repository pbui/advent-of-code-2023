#!/usr/bin/env python3

''' Day 02 - Part A '''

from collections import defaultdict
from typing      import Iterator
import sys

# Types

Game = dict[str, int]

# Constants

RED_MAX   = 12
GREEN_MAX = 13
BLUE_MAX  = 14

# Functions

def read_game(stream=sys.stdin) -> Game:
    try:
        game_string, cubes_string = stream.readline().split(':')
    except ValueError:
        return {}

    game: Game = defaultdict(int)
    game['id'] = int(game_string.split()[-1])

    for cubes in cubes_string.split(';'):
        for cube in cubes.split(','):
            count, color = cube.split()
            game[color] = max(game[color], int(count))

    return game

def read_games(stream=sys.stdin) -> Iterator[Game]:
    while game := read_game(stream):
        yield game

def is_valid_game(game: Game) -> bool:
    return all([
        game['red']   <= RED_MAX,
        game['green'] <= GREEN_MAX,
        game['blue']  <= BLUE_MAX,
    ])

# Main Execution

def main(stream=sys.stdin) -> None:
    valid_games = filter(is_valid_game, read_games(stream))
    sum_of_ids  = sum(game['id'] for game in valid_games)
    print(sum_of_ids)

if __name__ == '__main__':
    main()
