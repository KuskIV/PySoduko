from SodukoClass import Soduko
import OpenFile as of
import ThroughSoduko as solve
import sys
import time
import get
import check
import exhaust

sys.setrecursionlimit(10000)
start_time = time.time()

soduko = Soduko("soHard")

#soduko.Print(soduko)
solve.Soduko(soduko)

soduko.Print(soduko)

if soduko.verify(soduko):
    print("\nStatus           : SUCCESS!")
    print("Completiong time : {0:.3f}  sec".format(time.time() - start_time))
else:
    print("\nStatus : FAILED")


