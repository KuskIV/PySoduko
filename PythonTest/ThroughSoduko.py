import Position as po
import Line_values as lv
import math
import Line_length as ll
import SodukoClass
import OpenFile as of
import enum_val as e_val
from MakeTestSoduko import Soduko_func as s_func
import update_soduko as us


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


def possible_matche(down, right, soduko):
    return soduko.S[down][right] == 0
    
def try_down(soduko, down, right):
    pos_list = ll.get_empty_pos_down(soduko, down, right)
    exclude_list = []
    for pos in pos_list:
        #this does not work. get list from a point
        exclude_list.append(soduko.pos_val.get(e_val.Direction.Down)[pos[1]])
    print(f"down : {exclude_list}")

def try_righ(soduko, down, right):
    return False

def try_square(soduko, down, right):
    return False

def solve_for_pos(soduko, down, right):
    if try_down(soduko, down, right):
        return True
    elif try_righ(soduko, down, right):
        return True
    elif try_square(soduko, down, right):
        return True
    return False


def done(length, n, pos):
    return n > length and pos > length ** 2

def solve_soduko(soduko, n, pos):
    down = math.floor(pos / len(soduko.S))
    right = pos % len(soduko.S)
    limit_size = len(soduko.S) ** 2
    
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
        if solve_for_pos(soduko, down, right):
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

first_run(soduko)
#second_run(soduko)
solve_for_pos(soduko, 0, 0)
s_func.Print(soduko)
print("done")
