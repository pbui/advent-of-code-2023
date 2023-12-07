#!/usr/bin/env python3

''' Day 07 - Part B '''

from collections import Counter
from enum        import IntEnum

import sys

# Constants

LABELS = {l: v for v, l in enumerate('J23456789TQKA', 1)}

# Classes

class HandType(IntEnum):
    FIVE_OF_A_KIND  = 6
    FOUR_OF_A_KIND  = 5
    FULL_HOUSE      = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR        = 2
    ONE_PAIR        = 1
    HIGH_CARD       = 0

class Hand:
    def __init__(self, cards=str, bid=str):
        self.cards  = cards
        self.bid    = int(bid)
        counts      = Counter(self.cards)

        if 'J' in counts and len(counts) > 1:
            max_label = max(set(counts) - {'J'}, key=lambda l: (counts[l], LABELS[l]))
            counts[max_label] += counts['J']
            del counts['J']

        self.type   = (
            HandType.FIVE_OF_A_KIND  if len(counts) == 1 else
            HandType.FOUR_OF_A_KIND  if len(counts) == 2 and any(l for l, count in counts.items() if count == 4) else
            HandType.FULL_HOUSE      if len(counts) == 2 and any(l for l, count in counts.items() if count == 3) else
            HandType.THREE_OF_A_KIND if len(counts) == 3 and any(l for l, count in counts.items() if count == 3) else
            HandType.TWO_PAIR        if len(counts) == 3 and any(l for l, count in counts.items() if count == 2) else
            HandType.ONE_PAIR        if len(counts) == 4 and any(l for l, count in counts.items() if count == 2) else
            HandType.HIGH_CARD
        )

    def __lt__(self, other):
        if self.type == other.type:
            for s_label, o_label in zip(self.cards, other.cards):
                if LABELS[s_label] == LABELS[o_label]:
                    continue
                return LABELS[s_label] < LABELS[o_label]
            return False
        return self.type < other.type

    def __repr__(self):
        return f'Hand(cards={self.cards},bid={self.bid},type={self.type})'

# Functions

def read_hands(stream=sys.stdin) -> list[Hand]:
    return [Hand(*line.split()) for line in stream]

# Main Execution

def main(stream=sys.stdin) -> None:
    hands    = sorted(read_hands(stream))
    winnings = sum(rank * hand.bid for rank, hand in enumerate(hands, 1))
    print(winnings)

if __name__ == '__main__':
    main()
