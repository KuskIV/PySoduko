
import numpy as np
from SodukoClass import Soduko

def remove_values_from_list(num_list, val):
   return [value for value in num_list if value != val]

def square_line(rel_y, rel_x, pos, soduko):
    i = 0
    line = []
    while i < soduko.squareSize:
        posy = pos[0] - rel_y + i
        posx = rel_x
        line.append(int(soduko.S[posx][posy])) 
        i += 1 

    return line

def down_line(down, soduko, start, end):
    """Find values down"""
    line = []

    for n in range(start, end):
        line.append(int(soduko.S[n][down]))
    return line

def right_line(right, soduko, I_start, I_end):
    """Find value right"""
    line = []
    for n in range(I_start, I_end):
        line.append(int(soduko.S[right][n]))
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

def zero_right_line(right, soduko):
    line = right_line(right, soduko, 0, len(soduko.S) - 1)
    return remove_values_from_list(line, 0)

def zero_down_line(down, soduko):
    line = down_line(down, soduko, 0, len(soduko.S) -1 )
    return remove_values_from_list(line, 0)

def zero_square(rel_pos, pos, soduko):
    line = square(rel_pos, pos, soduko, 0, soduko.squareSize)
    return remove_values_from_list(line, 0)

def zero_pos_right(right, soduko, n):
    line = right_line(right, soduko, n, n + 1)
    result = []
    for n in line:
        if n == 0:
            result.append(n)
    return result

def zero_pos_down(down, soduko, n):
    line = down_line(down, soduko, n, n)
    result = []
    for n in line:
        if n == 0:
            result.append(n)
    return result
