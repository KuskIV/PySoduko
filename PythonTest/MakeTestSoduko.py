import numpy as np
import SodukoClass

class Soduko_func(object):
    """description of class"""

    @staticmethod
    def Create(square_size, p_list):
        sodukoSize = square_size ** 2

        S = np.zeros((sodukoSize, sodukoSize))

        for p in p_list:
            S[p[1]][p[0]] = p[2]

        return S

    @staticmethod
    def Print(S):

        bottom_line = S.bottom_line
        
        print(f"\n{bottom_line}")
        for r in S.S:
            print("| ", end = "")
            for n in r:
                if int(n) is 0:
                    print(" ", end = " | ")
                else:
                    print(str(int(n)).zfill(S.number_size), end = " | ")
            print(f"\n{bottom_line}")

    @staticmethod
    def Print_small(S, b_line):

        bottom_line = b_line * len(S) + "-"
        
        print(f"\n{bottom_line}")
        for r in S:
            print("| ", end = "")
            for n in r:
                print(int(n), end = " | ")
            print(f"\n{bottom_line}")

    @staticmethod
    def Is_verified(S):

        if len(S) == 0:
            print("The squaresize cannot be zero")
            return False
        elif len(S) > 25:
            print("This soduko is way too big")
            return False
        else:
            print("Soduko is accepted! It will now be solved, behold!")
            return True
        