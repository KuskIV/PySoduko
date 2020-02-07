from enum_val import Direction
import get
import check

def down(soduko, down, right, n):
    if len(soduko.S) - len(soduko.pos_val[Direction.Down][down]) <= n:
        pos_list = get.empty_pos_down(soduko, down, right)
        viable_list = get.values_for_pos(down, right, soduko)
        if check.viable_list(down, right, soduko, viable_list):
            return True
        if check.excluded_list(down, right, soduko, pos_list, viable_list, Direction.Down):
            return True
    return False

def right(soduko, down, right, n):
    if len(soduko.S) - len(soduko.pos_val[Direction.Right][down]) <= n:
        pos_list = get.empty_pos_right(soduko, down, right)
        viable_list = get.values_for_pos(down, right, soduko)
        if check.viable_list(down, right, soduko, viable_list):
            return True
        if check.excluded_list(down, right, soduko, pos_list, viable_list, Direction.Right):
            return True
    return False

def square(soduko, down, right, n):
    if len(soduko.S) - len(soduko.pos_val[Direction.Right][down]) <= n:
        pos_list = get.empty_pos_square(soduko, down, right)
        viable_list = get.values_for_pos(down, right, soduko)
        if check.viable_list(down, right, soduko, viable_list):
            return True
        if check.excluded_list(down, right, soduko, pos_list, viable_list, Direction.Square):
            return True
    return False