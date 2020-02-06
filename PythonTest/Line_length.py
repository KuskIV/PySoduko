import numpy as np
from SodukoClass import Soduko
from MakeTestSoduko import Soduko_func as s_func
import OpenFile as of
import enum_val

def down_line_length(down, soduko):
    """Takes a row down"""
    length = []
    for n in range(0, len(soduko.S)):
        if soduko.S[n][down] == 0:
            length.append([n, down])
    return length

def get_empty_pos_down(soduko, down, right):
    result = down_line_length(right, soduko)
    if not [down, right] in result:
        #print("-----------------------------------------")
        print(result)
        print(f"down {down} right {right} val {soduko.S[down][right]}")
        #print(soduko.pos_val[enum_val.Direction.Down])
        #print(soduko.pos_val[enum_val.Direction.Right])
        #print(soduko.pos_val[enum_val.Direction.Square])
        #print(soduko.S)
        #print("-----------------------------------------")
    else:
        result.remove([down, right])
    return result

def right_line_length(right, soduko):
    """Takes a rown right"""
    length = []
    for n in range(0, len(soduko.S)):
        if soduko.S[right][n] == 0:
            length.append([right, n])
    return length

def get_empty_pos_right(soduko, down, right):
    result = right_line_length(down, soduko)
    result.remove([down, right])
    return result

def square_line_length(right, down, pos, soduko):
    i = 0
    length = []
    rel_pos = 0
    while i < soduko.squareSize:
        rel_pos = pos[1] - right + i
        if int(soduko.S[down][rel_pos]) == 0:
            length.append([down, rel_pos])
        i += 1 

    return length

def square_length(rel_pos, pos, soduko):
    square = np.zeros((soduko.squareSize, soduko.squareSize))
    i = 0
    length = []
    while i < len(square):
        down = pos[0] - rel_pos[0] + i
        length += square_line_length(rel_pos[1], down, pos, soduko)
        i += 1
    return length

def get_rel_pos(down, right, soduko):
    rel_pos = []
    rel_pos.append(down % soduko.squareSize)
    rel_pos.append(right % soduko.squareSize)
    return rel_pos

def get_empty_pos_square(soduko, down, right):
    rel_pos = get_rel_pos(down, right, soduko)
    result = square_length(rel_pos, [down, right], soduko)
    result.remove([down, right])
    return result