import os
import sys
import time
from Constants import Constants



s = "aaron"
for count in range(1000) :
    for i in range(3):
        print(s)
    time.sleep(2)
    print("\033[4F")
    time.sleep(2)
    for i in range(3):
        print(Constants.COLOR.RED+s+Constants.COLOR.ENDC)
    time.sleep(2)
    print("\033[4F")


# print("bye")


  