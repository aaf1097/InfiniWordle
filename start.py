from queue import Empty
import random
import sys
from Constants import Constants
from Words import Words
from Printer import KeyBoard


print("Start")
word = Words()
worldList = word.getWordList()

chosenWord = []
chosenWord[:0] = random.choice(worldList)
wordSize = len(chosenWord)

keyboard = KeyBoard()


# print(str(chosenWord))

unusableLetters = []
for i in range(Constants.maxTries) :
    if unusableLetters :
        keyboard.keyboardPrinter(unusableLetters)
    
    value = input("Guess " + str(i+1) + " : ")
    ipList = []
    ipList[:0] = value
    flag = True
    y = 0

    for currentLetter in ipList :
        if currentLetter in chosenWord :
            if currentLetter == chosenWord[y] :
                print(Constants.COLOR.GREEN + currentLetter + Constants.COLOR.ENDC, end ="")
            else :
                print(Constants.COLOR.YELLOW + currentLetter + Constants.COLOR.ENDC, end ="")
                flag = False
        else :
            print(Constants.COLOR.RED + currentLetter  + Constants.COLOR.ENDC, end ="")
            if not currentLetter in unusableLetters :
                unusableLetters.append(currentLetter) 
            flag = False
        y += 1

    print()


    if flag == True :
        print("Game Won")
        sys.exit(0)


print("Game Over!")
print(chosenWord)    
