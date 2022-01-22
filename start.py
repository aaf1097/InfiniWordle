from queue import Empty
import random
import sys
from tkinter import *
from Constants import Constants
from Words import Words

print("Start")
word = Words()
worldList = word.getWordList()

chosenWord = []
chosenWord[:0] = random.choice(worldList)
wordSize = len(chosenWord)

# print(str(chosenWord))
# print(wordSize)
unusableLetters = []
for i in range(Constants.maxTries) :
    if unusableLetters :
        print(Constants.COLOR.RED + "Unusable letters are :\n" + str(unusableLetters) + Constants.COLOR.ENDC)
        print()
    
    value = input("Guess " + str(i+1) + " : ")
    ipList = []
    ipList[:0] = value
    flag = True
    y = 0
    for currentLetter in ipList :
        if currentLetter in chosenWord :
            if currentLetter == chosenWord[y] :
                print(Constants.COLOR.GREEN + currentLetter +" character good at position : " + str(y) + Constants.COLOR.ENDC)
            else :
                print(Constants.COLOR.YELLOW + currentLetter + " is present in the word but position is wrong" + Constants.COLOR.ENDC)
                flag = False
        else :
            print(Constants.COLOR.RED + currentLetter + " is not present in the word" + Constants.COLOR.ENDC)
            if not currentLetter in unusableLetters :
                unusableLetters.append(currentLetter)
            flag = False
        y += 1

    if flag == True :
        print("Game Won")
        sys.exit(0)


print("Game Over!")
print(chosenWord)    

# master = Tk()
# w = Canvas(master, width=40, height=60)
# w.pack()
# canvas_height=20
# canvas_width=200
# y = int(canvas_height / 2)
# w.create_line(0, y, canvas_width, y )
# mainloop()
