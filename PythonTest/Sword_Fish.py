import SodukoClass
import check
import math
from Points import Point
import get
import numpy as np
import itertools as it
import collections
import copy

def find_empty_points(soduko):
    points = []
    for pos in range(0, len(soduko.S) ** 2):
        down = math.floor(pos / len(soduko.S))
        right = pos % len(soduko.S)
        if soduko.S[down][right] == 0:
            points.append(Point([down, right], check.revert_list(get.values_for_pos(down, right, soduko), soduko)))
    return points

def find_viable_points(pos_arr, dir, value):
    result = []
    for pos in pos_arr:
        if pos.position[dir] == value:
            result.append(pos)
    return result

def find_values_in_lists(pos_arr):
    result = []
    for pos in pos_arr:
        result.append(pos.viable_values)
    result = list(it.chain.from_iterable(result))
    result = list(dict.fromkeys(result))
    return result
    
def count_val_in_arr(pos_arr, soduko):
    values_in_lists = find_values_in_lists(pos_arr)
    val_res = []
    result = {}
    count = 0
    for val in values_in_lists:
        count = 0
        del val_res[:]
        for pos in pos_arr:
            if val in pos.viable_values:
                count += 1
            if count <= 2 and val in pos.viable_values:
                val_res.append(pos.position)
            if count > 2:
                val_res.clear()
                break
        if len(val_res) != 0:
            temp_dict = {val:list(val_res)}
            result.update(temp_dict)
    return result           

def find_possible_swordfish(pos_dict):
    result = {}
    for i in pos_dict.keys():
        for key in pos_dict.keys():
            for j in pos_dict[key].keys():
                if key > i:
                    if j in pos_dict[i].keys():
                        if j in result:
                            to_add = pos_dict[i].get(j) + pos_dict[key].get(j)
                            for to in to_add:
                                if not to in result[j]:
                                    result[j].append(to)
                        else:
                            add_new = {j:pos_dict[i].get(j) + pos_dict[key].get(j)}
                            result.update(add_new)
    return result
            
def print_dict(sword_dict):
    for key in sword_dict:
        print(f"value {key} in {sword_dict[key]}")

def setup_arr(empty_points, soduko, directoin):
    result = {}
    for row in range(0, len(soduko.S)):
        arr = list(find_viable_points(empty_points, directoin, row))
        dict_to_add = count_val_in_arr(arr, soduko)
        if bool(dict_to_add):
            temp_dict = {row:dict(dict_to_add)}
            result.update(temp_dict)
    return result

def find_swordfish(res_dict, dir):
    result = {}
    for i in res_dict:
        check_list = []
        if len(res_dict[i]) == 6:
            for val in res_dict[i]:
                check_list.append(val[dir])
            if len(list(dict.fromkeys(check_list))) == 3:
                temp = {i:copy.deepcopy(res_dict[i])}
                result.update(temp)
        elif len(res_dict[i]) > 6:
            print(f"value {i} is longer than 6 ({res_dict[i]})")
    return result

def find(soduko):
    empty_points = find_empty_points(soduko)
    right_dict = {}
    right_res_dict = {}

    right_dict = setup_arr(empty_points, soduko, 0)
    right_res_dict = find_possible_swordfish(right_dict)
    right_res_dict = find_swordfish(right_res_dict, 1)
    if bool(right_res_dict):
        print("a swordfish was found right")
        print_dict(right_res_dict)
    else:
        print("a swordfish was not found right")

    down_dict = {}
    down_res_dict = {}

    down_dict = setup_arr(empty_points, soduko, 1)
    down_res_dict = find_possible_swordfish(down_dict)
    down_res_dict = find_swordfish(down_res_dict, 0)
    if bool(down_res_dict):
        print("a swordfish was found down")
        print_dict(down_res_dict)
    else:
        print("a swordfish was not found down")