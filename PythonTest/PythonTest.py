from SodukoClass import Soduko
import OpenFile as of
import ThroughSoduko as solve
import sys
import time
import get
import check
import exhaust
import Sword_Fish
from CleverExhaust import assignValues

sys.setrecursionlimit(10000)
start_time = time.time()

soduko = Soduko("soThree")

soduko.Print(soduko)

solve.Soduko(soduko)

soduko.Print(soduko)

#stuff = assignValues(soduko)
#for pos in stuff:
#    print(f"{pos.position} -> {pos.viable_values}")
#Sword_Fish.find(soduko)


if soduko.verify(soduko):
    print("\nStatus           : SUCCESS!")
    print("Completiong time : {0:.3f}  sec".format(time.time() - start_time))
else:
    print("\nStatus : FAILED")


