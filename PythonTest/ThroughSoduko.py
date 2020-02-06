import Position as po
import Line_values as lv
import math
import Line_length as ll
import SodukoClass
import OpenFile as of
import enum_val as e_val
from MakeTestSoduko import Soduko_func as s_func
import update_soduko as us
import numpy as np
from itertools import chain
import sys


def first_run(soduko):
    us.setup_dict(soduko)
    us.update_rigt_arr(soduko)
    us.update_down_arr(soduko)
    us.update_square_arr(soduko)



def check_one(num_list, n, max_size, s_index):
    for e in range(s_index, max_size):
        if max_size - len(num_list[e]) == n:
            return (num_list[e], e)
    return None, 0

def revert_list(input_list, soduko):
    result = []
    for i in range(1, len(soduko.S) + 1):
        if not i in input_list:
            result.append(i)
    return result


def possible_matche(down, right, soduko):
    return soduko.S[down][right] == 0

def two_dim_to_unique(arr):
    arr = list(chain.from_iterable(arr))
    arr = list(dict.fromkeys(arr))
    return arr

def get_square_number(down, right, squareSize):
    down_val = math.ceil((down + 1) / squareSize)
    right_val = math.ceil((right + 1) / squareSize)
    return (3 * down_val - (3 - right_val)) - 1

def get_values_for_pos(down, right, soduko):
    result = []
    result.append(soduko.pos_val.get(e_val.Direction.Down)[right])
    result.append(soduko.pos_val.get(e_val.Direction.Right)[down])
    square_val = get_square_number(down, right, soduko.squareSize)
    result.append(soduko.pos_val.get(e_val.Direction.Square)[square_val])
    return two_dim_to_unique(result)

def revert_val_for_pos(down, right, soduko):
    return revert_list(get_values_for_pos(down, right, soduko), soduko)


def update_one_pos(soduko, down, right, new_val):
    soduko.pos_val[e_val.Direction.Down][down].append(new_val) 
    soduko.pos_val[e_val.Direction.Right][down].append(new_val)
    soduko.pos_val[e_val.Direction.Square][down].append(new_val)

def check_viable_list(down, right, soduko, viable_list):
    viable_list = revert_list(viable_list, soduko)
    if len(viable_list) is 1:
        soduko.S[down][right] = viable_list[0]
        update_one_pos(soduko, down, right, viable_list[0])
        return True
    return False

def check_excluded_list(down, right, soduko, pos_list, viable_list, dir):
    exclude_list = []
    for pos in pos_list:
        exclude_list.append(revert_val_for_pos(pos[0], pos[1], soduko))
    exclude_list = two_dim_to_unique(exclude_list)
    exclude_list = revert_list(exclude_list, soduko)
    exclude_list = remove_exiting_objects(exclude_list, soduko.pos_val[dir][right])
    if len(exclude_list) is 1:
        if exclude_list[0] in viable_list:
            soduko.S[down][right] = exclude_list[0]
            update_one_pos(soduko, down, right, exclude_list[0])
            return True
    return False
    
def try_down(soduko, down, right, n):
    if len(soduko.S) - len(soduko.pos_val[e_val.Direction.Down][down]) <= n:
        pos_list = ll.get_empty_pos_down(soduko, down, right)
        viable_list = get_values_for_pos(down, right, soduko)
        if check_viable_list(down, right, soduko, viable_list):
            return True
        if check_excluded_list(down, right, soduko, pos_list, viable_list, e_val.Direction.Down):
            return True
    return False

def remove_exiting_objects(input_list, check_list):
    result = []
    for item in check_list:
        if not item in input_list:
            result.append(item)
    return result

def try_right(soduko, down, right, n):
    if len(soduko.S) - len(soduko.pos_val[e_val.Direction.Right][down]) <= n:
        pos_list = ll.get_empty_pos_right(soduko, down, right)
        viable_list = get_values_for_pos(down, right, soduko)
        if check_viable_list(down, right, soduko, viable_list):
            return True
        if check_excluded_list(down, right, soduko, pos_list, viable_list, e_val.Direction.Right):
            return True
    return False


def try_square(soduko, down, right, n):
    if len(soduko.S) - len(soduko.pos_val[e_val.Direction.Right][down]) <= n:
        pos_list = ll.get_empty_pos_square(soduko, down, right)
        viable_list = get_values_for_pos(down, right, soduko)
        if check_viable_list(down, right, soduko, viable_list):
            return True
        if check_excluded_list(down, right, soduko, pos_list, viable_list, e_val.Direction.Square):
            return True
    return False

def solve_for_pos(soduko, down, right, n):
    if try_down(soduko, down, right, n):
        return True
    elif try_right(soduko, down, right, n):
        return True
    elif try_square(soduko, down, right, n):
        return True
    return False


def done(length, n, pos):
    return n > length and pos > length ** 2

def solve_soduko(soduko, n, pos):
    down = math.floor(pos / len(soduko.S))
    right = pos % len(soduko.S)
    limit_size = len(soduko.S) ** 2

    if n == len(soduko.S):
        return True
    if done(len(soduko.S), n, pos):
        # If n has reached the limit, and all positions have been gone through
        # should be done, return true
        return True
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

txt_soduko = of.return_soduko_from_file("sOne")
soduko = SodukoClass.Soduko(txt_soduko)

sys.setrecursionlimit(10000)
first_run(soduko)
second_run(soduko)
s_func.Print(soduko)
print("done")
