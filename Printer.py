from Constants import Constants

class KeyBoard :
    keyboard = {}
    aphabetsString = "QWERTYUIOPASDFGHJKLZXCVBNM"
    keysList = []
    keysList[:0] = aphabetsString
    for alph in keysList :
        keyboard[alph] = True


    def keyboardPrinter(self, keys) :
        
        for key in keys : 
            key = key.upper()
            self.keyboard[key] = False

        def printKeyVal(keyboardDict, key) :
            if self.keyboard[key] == True :
                return key
            else :
                return Constants.COLOR.RED + key + Constants.COLOR.ENDC
    
        for key in self.keyboard : 
            if key == "P" : 
                print(printKeyVal(self.keyboard, key))
                print(" " , end = " ")
            elif key == "L" :
                print(printKeyVal(self.keyboard, key))
                print("  " , end = " ")
            elif key == "M" :
                print(printKeyVal(self.keyboard, key))
            else :
                print(printKeyVal(self.keyboard, key), end =" ")



