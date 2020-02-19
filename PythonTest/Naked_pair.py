import math
import get

"""
def find_next_val(soduko, limit, start):
    for pos in range(start, len(soduko.S) ** 2):
        down = math.floor(pos / len(soduko.S))
        right = pos % len(soduko.S)
        if pos > limit:
            return None
        if soduko[down][right] == 0:
            return [down, right]


def find_naked_pair(soduko):
    for pos in range(0, len(soduko.S) ** 2):
        down = math.floor(pos / len(soduko.S))
        right = pos % len(soduko.S)
        current_val = soduko.S[down][right]
        if current_val == 0:
            next_val = find_next_val(soduko, 0, pos + 1)
            if next_val == 0 and current_val % soduko.squareSize == next_val % soduko.squareSize:
                print()
"""