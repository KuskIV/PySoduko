from SodukoClass import Soduko
import MakeTestSoduko as ms
import Line_length as ll
import Line_values as lv
import numpy as np
from enum import Enum

"""
def FindIndexHandleZero(p, squareSize):
    return p % squareSize


def FindPositionInSquare(posXY, squareSize):
    return (FindIndexHandleZero(posXY[0], squareSize), FindIndexHandleZero(posXY[1],squareSize))


def get_reverse(i_list, count):
    r_list = []

    for n in range(1, count + 1):
        if not n in i_list:
            r_list.append(n)

    return r_list


def list_of_positions(posXY, soduko):
    currentPos = FindPositionInSquare(posXY, soduko.squareSize)
    result = []

    result.append(lv.right_line(posXY[1], soduko, 0, len(soduko.S))) 
    result.append(lv.down_line(posXY[0], soduko, 0, len(soduko.S)))
    result.append(lv.square(currentPos, posXY, soduko, 0, len(soduko.S)))
    return result


def min_lengt_of_positions(posXY, soduko):
    currentPos = FindPositionInSquare(posXY, soduko.squareSize)
    length = []

    length.append(ll.right_line_length(posXY[1], soduko))
    length.append(ll.down_line_length(posXY[0], soduko))
    length.append(ll.square_length(currentPos, posXY, soduko))

    return min(length)

def all_lengt_of_positions(posXY, soduko):
    currentPos = FindPositionInSquare(posXY, soduko.squareSize)
    length = []

    length.append(ll.right_line_length(posXY[1], soduko))
    length.append(ll.down_line_length(posXY[0], soduko))
    length.append(ll.square_length(currentPos, posXY, soduko))

    return length
    """
