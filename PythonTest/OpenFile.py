
import numpy as np
import math

def arr_to_soduko(arr):
    line_size = int(math.sqrt(len(arr) - 1))
    square_size = int(math.sqrt(line_size))
    soduko = np.zeros((line_size, line_size))

    for n in range(0, len(arr) - 1):
        if n != "":
            soduko[math.floor(n / line_size)][n % line_size] = arr[n]
    return soduko


def return_soduko_from_file(sName):
    f = open(f"SodukoFiles/sOne.txt", "r")
    content = f.read()
    f.close()
    arr = content.split(" ")
    return arr_to_soduko(arr)