from Constants import Constants

class KeyBoard :
    keyboard = {}
    aphabetsString = "QWERTYUIOPASDFGHJKLZXCVBNM"
    keysList = []
    keysList[:0] = aphabetsString
    for alph in keysList :
        keyboard[alph] = 'WHITE'


    def keyboardPrinter(self) :
        
        # for key in keys : 
        #     key = key.upper()
        #     self.keyboard[key] = 'WHITE'

        def printKeyVal(keyboardDict, key) :
            if self.keyboard[key] == 'WHITE':
                return key
            elif self.keyboard[key] == 'RED':
                return Constants.COLOR.RED + key + Constants.COLOR.ENDC
            elif self.keyboard[key] == 'YELLOW':
                return Constants.COLOR.YELLOW + key + Constants.COLOR.ENDC
            elif self.keyboard[key] == 'GREEN':
                return Constants.COLOR.GREEN + key + Constants.COLOR.ENDC
            
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
