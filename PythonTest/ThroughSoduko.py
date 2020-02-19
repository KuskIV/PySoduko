import math
import SodukoClass
import OpenFile as of
from enum_val import Direction
import update_soduko as us
import numpy as np
from itertools import chain
import sys
import time
import solve
import exhaust
from CleverExhaust import exhaust


def first_run(soduko):
    us.setup_dict(soduko)
    us.update_rigt_arr(soduko)
    us.update_down_arr(soduko)
    us.update_square_arr(soduko)


def possible_matche(down, right, soduko):
    return soduko.S[down][right] == 0

def solve_for_pos(soduko, down, right, n):
    if solve.down(soduko, down, right, n):
        return True
    elif solve.right(soduko, down, right, n):
        return True
    elif solve.square(soduko, down, right, n):
        return True
    return False

def done(length, n, pos):
    return n > length and pos > length ** 2

def solve_soduko(soduko, n, pos):
    down = math.floor(pos / len(soduko.S))
    right = pos % len(soduko.S)
    limit_size = len(soduko.S) ** 2

    if n == len(soduko.S):
        return soduko
    if done(len(soduko.S), n, pos):
        # If n has reached the limit, and all positions have been gone through
        # should be done, return true
        return soduko
    elif pos >= limit_size:
        # If all positions has been gone through for one n
        # cound n up and reset pos
        return solve_soduko(soduko, n + 1, 0)
    elif possible_matche(down, right, soduko):
        # If the positions is not 0 try and find a solution
        if solve_for_pos(soduko, down, right, n):
            # If a solution is found, reset the position
            return solve_soduko(soduko, n, 0)
        #if a solution is not found, continue
        return solve_soduko(soduko, n, pos + 1)
    else:
        #If the number in pos is not 0, keep goint
        return solve_soduko(soduko, n, pos + 1)

def second_run(soduko):
    return solve_soduko(soduko, 1, 0)

def Soduko(soduko):
    first_run(soduko)
    second_run(soduko)
    #if not soduko.verify(soduko):
    #    print("Engage exhaust. State:")
    #    soduko.Print(soduko)
    #    exhaust(soduko)
    #    exhaust.Soduko(soduko)