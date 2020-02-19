import math
from enum_val import Direction
import OpenFile as of

class Soduko:
    """Called to verify Soduko"""
    
    @staticmethod
    def num_line(self_sod):
        return (self_sod.number_size * len(self_sod.S)) * "-"

    @staticmethod
    def standard_line(self_sod):
        return "---" * len(self_sod.S) + "-"

    @staticmethod
    def make_line(S):
        return Soduko.num_line(S) + Soduko.standard_line(S)

    @staticmethod
    def verify_part(key, soduko):
        for l in soduko.pos_val[key]:
            if not (len(l) == len(set(l))) or not len(l) is len(soduko.S):
                return False
        return True

    @staticmethod
    def verify(soduko):
        if not Soduko.verify_part(Direction.Down, soduko):
            return False
        elif not Soduko.verify_part(Direction.Right, soduko):
            return False
        elif not Soduko.verify_part(Direction.Square, soduko):
            return False
        else:
            return True

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


    def __init__(self, s_name):
        self.S = of.return_soduko_from_file(s_name)
        self.squareSize = int(math.sqrt(len(self.S)))
        self.number_size = len(str(len(self.S)))
        self.bottom_line = Soduko.make_line(self)
        self.pos_val = {}
        self.excluded_dict = {}

