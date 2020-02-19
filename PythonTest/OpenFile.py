
import numpy as np
import math

def arr_to_soduko(arr):
    line_size = int(math.sqrt(len(arr)))
    soduko = np.zeros((line_size, line_size))
    for n in range(0, len(arr)):
        if n != "":
            soduko[math.floor(n / line_size)][n % line_size] = arr[int(n)]
    return soduko


def return_soduko_from_file(sName):
    f = open(f"PythonTest/SodukoFiles/{sName}.txt", "r")
    content = f.read()
    f.close()
    arr = content.split(" ")
    return arr_to_soduko(arr)