import Position as po
import Line_values as lv
import math
import Line_length as ll

def update_rigt_arr(soduko):
    del soduko.right_arr[:]
    for n in range(0, len(soduko.S)):
        soduko.right_arr.append(lv.zero_right_line(n, soduko))  
    soduko.right_arr.sort(key = len)

def update_down_arr(soduko):
    del soduko.down_arr[:]
    for n in range(0, len(soduko.S)):
        soduko.down_arr.append(lv.zero_down_line(n, soduko))
    soduko.down_arr.sort(key = len)
def update_square_arr(soduko):
    del soduko.squares_arr[:]
    sq = soduko.squareSize
    for n in range(0, sq):
        for p in range(0, sq):
            pos = ((p % sq) * sq, (n % sq) * sq)
            rel = (0,0)
            soduko.squares_arr.append(lv.zero_square(rel, pos, soduko))
    soduko.squares_arr.sort(key = len)


def first_run(soduko):
    update_rigt_arr(soduko)
    update_down_arr(soduko)
    update_square_arr(soduko)

def check_one(num_list, n, max_size, s_index):
    for e in range(s_index, max_size):
        if max_size - len(num_list[e]) == n:
            return (num_list[e], e)
    return None, 0

def find(test_arr, soduko, n, s_index):
    Lres = []
    Ires = 0
    size = len(soduko.S)

    if n >= size:
        return False
    Lres, Ires = check_one(test_arr, n, size, s_index)
    if not Lres is None:
        return find(test_arr, soduko, n, Ires + 1)
    else:
        return find(test_arr, soduko, n + 1, 0)

def solve_position(soduko, n, down, right):
    print(f"{soduko.S[down][right]}, n = {n}")

def possible_matche(down, right, soduko, n):
    posXY = [down, right]
    return soduko.S[down][right] == 0
    #return soduko.S[down][right] == 0 and n in po.all_lengt_of_positions(posXY, soduko)

def set_n(n):
    return n - 1 if n - 1 >= 1 else 1

def solve_soduko(soduko, n, pos):
    down = math.floor(pos / len(soduko.S))
    right = pos % len(soduko.S)
    
    print(f"n = {n}, pos = {pos}, { len(soduko.S) ** 2 - 1}")
    if  (pos >= len(soduko.S) ** 2 - 1 and n >= len(soduko.S)) or n >= len(soduko.S):
        #solve_position(soduko, n, down, right)
        return True
    elif possible_matche(down, right, soduko, n):
        return solve_soduko(soduko, n, pos + 1)
        
    elif pos < len(soduko.S) ** 2 - 1:
        return solve_soduko(soduko, n, pos + 1)
    else:
        return solve_soduko(soduko, n + 1, 0)

def second_run(soduko, n):
    return solve_soduko(soduko, n, 0)
    #find(soduko.down_arr, soduko, n, 0)
    #find(soduko.right_arr, soduko, n, 0)
    #find(soduko.squares_arr, soduko, n, 0)

