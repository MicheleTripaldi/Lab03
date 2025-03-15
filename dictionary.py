class Dictionary:
    def __init__(self,dizionario =[]):
        self.dizionario = dizionario

    #def __contains__(self, word):
        #for parola in self.dizionario:
           # if parola == word:
                #return True

    def loadDictionary(self,path):
        with open(path,"r",encoding="utf-8") as file:
            for line in file:
                self.dizionario.append(line.strip().lower())
        return self.dizionario


    def printAll(self):
        print(self.dizionario)


    @property
    def dict(self):
        return self._dict