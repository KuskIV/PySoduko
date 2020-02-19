import math
from Points import Point
from SodukoClass import Soduko
from enum_val import Direction
import check
import get

def assignValues(soduko):
    points = []
    for pos in range(0, len(soduko.S) ** 2):
        down = math.floor(pos / len(soduko.S))
        right = pos % len(soduko.S)
        if soduko.S[down][right] == 0:
            points.append(Point([down, right], check.revert_list(get.values_for_pos(down, right, soduko), soduko)))
            #points.append(Point([down, right], check.revert_list(soduko.pos_val[Direction.Right][down], soduko)))
    return points


def exhaust(soduko):
    points = assignValues(soduko)
    for p in points:
        print(f"{p.position[0] + 1}, {p.position[1] + 1} - {p.viable_values}")