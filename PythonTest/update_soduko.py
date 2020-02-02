import enum_val as e_val
import Line_values as lv
from SodukoClass import Soduko

def print_dict(soduko):
    for x in soduko.pos_val:
        print(soduko.pos_val[x])

def update_rigt_arr(soduko):
    key = e_val.Direction.Right
    for n in range(0, len(soduko.S)):
        soduko.pos_val[key].append(lv.zero_right_line(n, soduko))


def update_down_arr(soduko):
    key = e_val.Direction.Down
    for n in range(0, len(soduko.S)):
        soduko.pos_val[key].append(lv.zero_down_line(n, soduko))


def update_square_arr(soduko):
    key = e_val.Direction.Square
    sq = soduko.squareSize
    for n in range(0, sq):
        for p in range(0, sq):
            pos = ((p % sq) * sq, (n % sq) * sq)
            rel = (0,0)
            soduko.pos_val[key].append(lv.zero_square(rel, pos, soduko))


def setup_dict(soduko):
    soduko.pos_val = {
        e_val.Direction.Down : [],
        e_val.Direction.Right : [],
        e_val.Direction.Square : []
    }