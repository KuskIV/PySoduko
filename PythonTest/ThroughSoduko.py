import Position as po
import Line_values as lv
import math
import Line_length as ll
import SodukoClass
import OpenFile as of
import enum_val as e_val
from MakeTestSoduko import Soduko_func as s_func

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


def first_run(soduko):
    setup_dict(soduko)
    update_rigt_arr(soduko)
    update_down_arr(soduko)
    update_square_arr(soduko)



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
        exclude_list.append(soduko.pos_val.get(e_val.Direction.Down)[pos[1]])
    print(exclude_list)

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
second_run(soduko)
get_empty_pos(soduko, 0, 0, 0)
s_func.Print(soduko)
print("done")
