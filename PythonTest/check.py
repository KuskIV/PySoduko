import enum_val as e_val
import get

def revert_list(input_list, soduko):
    result = []
    for i in range(1, len(soduko.S) + 1):
        if not i in input_list:
            result.append(i)
    return result

def update_one_pos(soduko, down, right, new_val):
    soduko.pos_val[e_val.Direction.Down][right].append(new_val) 
    soduko.pos_val[e_val.Direction.Right][down].append(new_val)
    soduko.pos_val[e_val.Direction.Square][get.square_number(down, right, soduko.squareSize)].append(new_val)

def revert_val_for_pos(down, right, soduko):
    return revert_list(get.values_for_pos(down, right, soduko), soduko)

def remove_exiting_objects(input_list, check_list):
    result = []
    for item in check_list:
        if not item in input_list:
            result.append(item)
    return result

def viable_list(down, right, soduko, viable_list):
    viable_list = revert_list(viable_list, soduko)
    if len(viable_list) is 1:
        soduko.S[down][right] = viable_list[0]
        update_one_pos(soduko, down, right, viable_list[0])
        return True
    return False

def excluded_list(down, right, soduko, pos_list, viable_list, dir):
    exclude_list = []
    for pos in pos_list:
        exclude_list.append(revert_val_for_pos(pos[0], pos[1], soduko))
    exclude_list = get.unique_list(exclude_list)
    exclude_list = remove_exiting_objects(exclude_list, revert_list(viable_list, soduko))
    if len(exclude_list) is 1:
        if not exclude_list[0] in viable_list:
            soduko.S[down][right] = exclude_list[0]
            update_one_pos(soduko, down, right, exclude_list[0])
            return True
    return False