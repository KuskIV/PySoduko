import get
from Points import Point
from itertools import permutations, product
import check
import copy

def find_all_points(soduko):
    points = get.all_empty_points(soduko)
    points_with_val = []
    for p in points:
        viable_val = get.shortest_way(p[0], p[1], soduko)
        temp = Point(p, viable_val)
        points_with_val.append(temp)
    return points_with_val

def all_length_list(input_list):
    result = []
    for p in input_list:
        i_len = []
        for i in range(0, len(p.viable_values)):
            i_len.append(i)
        result.append(i_len)
    return result

def exhaust_soduko(soduko, points, n, backup_dict, backup_soduko):
    count = 0
    need_to_check = True
    perm_list = all_length_list(points)
    for num in product(*perm_list):
        count += 1
        
        if count % 10000 == 0:
            print(f"count = {count}, still going strong!")

        soduko.pos_val = copy.deepcopy(backup_dict)
        soduko.S = backup_soduko.copy()
        for n in range(0, len(num)):
            need_to_check = True
            down = points[n].position[0]
            right = points[n].position[1]
            value = points[n].viable_values[num[n]]
            existing_valuese =  get.values_for_pos(down, right, soduko)
            if value in existing_valuese:
                need_to_check = False
                break
            else:
                check.update_one_pos(soduko, down, right, value)
                soduko.S[down][right] = value
        if need_to_check == True:
            if soduko.verify(soduko):
                break
    print(f"exhaust: done | count {count}")

def Soduko(soduko):
    backup_dict = copy.deepcopy(soduko.pos_val)
    backup_soduko = soduko.S.copy()
    all_points = find_all_points(soduko)
    exhaust_soduko(soduko, all_points, len(all_points), backup_dict, backup_soduko)
