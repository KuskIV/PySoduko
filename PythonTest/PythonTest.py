import SodukoClass
import Position as pos
from MakeTestSoduko import Soduko_func as s_func
import OpenFile as of
import ThroughSoduko as ts

posXY = (1,1)
txt_soduko = of.return_soduko_from_file("sOne")
soduko = SodukoClass.Soduko(txt_soduko)
not_solved = True
dead_end = False
first_run = True
soduko_edited = False

n = 1

if s_func.Is_verified(soduko.S):
    #print("\033c")
    ts.first_run(soduko)
    ts.second_run(soduko,+ n)
    s_func.Print(soduko)
