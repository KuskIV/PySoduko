import numpy as np
from SodukoClass import Soduko
from MakeTestSoduko import Soduko_func as s_func
import OpenFile as of

def down_line_length(down, soduko):
    """Takes a row down"""
    length = []
    for n in range(0, len(soduko.S)):
        if soduko.S[n][down] == 0:
            length.append([n, down])
    return length

def get_empty_pos_down(soduko, down, right):
    result = down_line_length(down, soduko)
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
    while i < soduko.squareSize:
        right = pos[0] - right + i
        if int(soduko.S[down][right]) == 0:
            length.append([down, right])
        i += 1 

    return length

def square_length(rel_pos, pos, soduko):
    square = np.zeros((soduko.squareSize, soduko.squareSize))
    i = 0
    length = []
    while i < len(square):
        down = pos[1] - rel_pos[1] + i
        length.append(square_line_length(rel_pos[0], down, pos, soduko))
        i += 1
    return length

def get_empty_pos_square(soduko, down, right):
    result = square_length([0,0], [down, right], soduko)
    result.remove([down, right])
    return result