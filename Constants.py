import os

class Constants :

    wordListPath = os.path.join(os.getcwd(),"wordList.txt")
    maxTries = 6

    class COLOR:
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'


