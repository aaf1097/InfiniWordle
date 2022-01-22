from Constants import Constants

class Words :
    
    path = Constants.wordListPath

    def getWordList(self) :
        with open(self.path,'r') as fileReader : 
            lines = fileReader.readlines()
        output = []
        for l in lines:
            output.append(l.replace("\n",""))
        return output

