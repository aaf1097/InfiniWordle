from queue import Empty
import random
import os
import sys
from Constants import Constants
from Words import Words
from Printer import KeyBoard

def PrintWord(guesses,keyboard=None):
    os.system('clear')
    print('''START''')
    for i in range(Constants.maxTries):
        if i<len(guesses):
            print(guesses[i])
        else:
            print("_____")
    keyboard.keyboardPrinter()
        
def secretword():
    word = Words()
    worldList = word.getWordList()
    chosenWord = []
    chosenWord[:0] = random.choice(worldList).upper()
    return chosenWord

def main():
    chosenWord = secretword()
    keyboard = KeyBoard()
    guesses = []
    PrintWord(guesses,keyboard=keyboard)
    for i in range(Constants.maxTries) :
        value = input(f'\033[{9-i}A')
        ipList = []
        ipList[:0] = value.upper()
        flag = True
        y = 0
        coloredguess = ''
        for currentLetter in ipList :
            if currentLetter in chosenWord :
                if currentLetter == chosenWord[y] :
                    coloredguess = coloredguess + Constants.COLOR.GREEN + currentLetter + Constants.COLOR.ENDC
                    keyboard.keyboard[currentLetter] = 'GREEN'
                else :
                    # FIXME (aaron): If alphabets repeat in the guess but not in the chosenWord,
                    # this will print repeated alphabets in yellow
                    coloredguess = coloredguess + Constants.COLOR.YELLOW + currentLetter + Constants.COLOR.ENDC
                    keyboard.keyboard[currentLetter] = 'YELLOW'
                    flag = False
            else :
                coloredguess = coloredguess + Constants.COLOR.RED + currentLetter  + Constants.COLOR.ENDC
                keyboard.keyboard[currentLetter] = 'RED' 
                flag = False
        y += 1
        guesses.append(coloredguess)
        PrintWord(guesses,keyboard)

    if flag == True :
        print("Game Won")
        sys.exit(0)

    print("Game Over!")
    print(''.join(chosenWord))

if __name__ == '__main__':
    main()