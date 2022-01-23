import os
import sys
import time
from Constants import Constants



s = "aaron"
def PrintWord(n,s):
    print(f'\033[{n}F' + s)
print(s)
for count in range(1000) :
    PrintWord(1,Constants.COLOR.RED+s+Constants.COLOR.ENDC)
    time.sleep(2)
    PrintWord(1,s)
    time.sleep(2)


# print("bye")


  
