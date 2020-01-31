import math
import MakeTestSoduko as m_soduko

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

    def __init__(self, soduko):
        self.S = soduko
        self.squareSize = int(math.sqrt(len(soduko)))
        self.number_size = len(str(len(self.S)))
        self.bottom_line = Soduko.make_line(self)
        self.squares_arr = []
        self.down_arr = []
        self.right_arr = []

