from enum_val import Direction
import math
from itertools import chain
import numpy as np
import check

def unique_list(arr):
    arr = list(chain.from_iterable(arr))
    arr = list(dict.fromkeys(arr))
    return arr

def square_number(down, right, squareSize):
    down_val = math.floor((down) / squareSize)
    right_val = math.floor((right) / squareSize)
    td = (squareSize * (down_val + 1)) - 1
    tr = squareSize - right_val - 1
    return td - tr

def values_for_pos(down, right, soduko):
    result = []
    result.append(soduko.pos_val.get(Direction.Down)[right])
    result.append(soduko.pos_val.get(Direction.Right)[down])
    square_val = square_number(down, right, soduko.squareSize)
    result.append(soduko.pos_val.get(Direction.Square)[square_val])
    return unique_list(result)

def down_line_empty(down, soduko):
    """Takes a row down"""
    length = []
    for n in range(0, len(soduko.S)):
        if soduko.S[n][down] == 0:
            length.append([n, down])
    return length

def empty_pos_down(soduko, down, right):
    result = down_line_empty(right, soduko)
    result.remove([down, right])
    return result

def right_line_empty(right, soduko):
    """Takes a rown right"""
    length = []
    for n in range(0, len(soduko.S)):
        if soduko.S[right][n] == 0:
            length.append([right, n])
    return length

def empty_pos_right(soduko, down, right):
    result = right_line_empty(down, soduko)
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

def empty_pos_square(soduko, down, right):
    rel_pos = get_rel_pos(down, right, soduko)
    result = square_length(rel_pos, [down, right], soduko)
    result.remove([down, right])
    return result

def remove_values_from_list(num_list, val):
   return [value for value in num_list if value != val]

def right_line(right, soduko, I_start, I_end):
    """Find value right"""
    line = []
    for n in range(I_start, I_end):
        line.append(int(soduko.S[right][n]))
    return line

def zero_right_line(right, soduko):
    line = right_line(right, soduko, 0, len(soduko.S))
    return remove_values_from_list(line, 0)

def down_line(down, soduko, start, end):
    """Find values down"""
    line = []

    for n in range(start, end):
        line.append(int(soduko.S[n][down]))
    return line

def zero_down_line(down, soduko):
    line = down_line(down, soduko, 0, len(soduko.S))
    return remove_values_from_list(line, 0)

def square_line(rel_y, rel_x, pos, soduko):
    i = 0
    line = []
    while i < soduko.squareSize:
        posy = pos[0] - rel_y + i
        posx = rel_x
        line.append(int(soduko.S[posx][posy])) 
        i += 1 

    return line

def square(rel_pos, pos, soduko, I_start, I_end):
    square = []
    i = I_start
    while i < I_end:
        posX = pos[1] - rel_pos[1] + i
        square = square + square_line(rel_pos[0], posX, pos, soduko)
        i += 1
    square = remove_values_from_list(square, 0)
    return square

def zero_square(rel_pos, pos, soduko):
    line = square(rel_pos, pos, soduko, 0, soduko.squareSize)
    return remove_values_from_list(line, 0)

def all_empty_points(soduko):
    result = []
    for i in range(0, len(soduko.S) ** 2):
        down = math.floor(i / len(soduko.S))
        right = i % len(soduko.S)
        if soduko.S[down][right] == 0:
            result.append([down, right])
    return result

def shortest_way(down, right, soduko):
    right_arr = check.revert_list(soduko.pos_val[Direction.Right][down], soduko)
    down_arr = check.revert_list(soduko.pos_val[Direction.Down][right], soduko) 
    square_arr = check.revert_list(soduko.pos_val[Direction.Square][square_number(down, right, soduko.squareSize)], soduko) 
    result = min([down_arr, right_arr, square_arr], key=len)
    exclude = values_for_pos(down, right, soduko)
    for n in exclude:
        if n in result:
            result.remove(n)
    return result

