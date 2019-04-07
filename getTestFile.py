import numpy as np


class TestFile :
    
    def __init__(self , filename):
        self.filename = filename
        self.data = None
        self.users = None
        self.places = None
        
    def extractUsersAndPlaces(self):
        inputFile = open(self.filename ,"r")
        allLines = inputFile.readlines()
        userId = 0 
        locId = 0
        for line in allLines :
            words = line.split()
            if words[0] not in self.users :
                self.users[words[0]] = userId
                userId += 1 
            if words[1] not in self.places :
                self.places[words[1]] = locId
                locId+=1

    def extract(self) :
        self.extractUsersAndPlaces()
        inputFile = open(self.filename ,"r")
        allLines = inputFile.readlines()
        self.data = np.zeros((len(self.users),len(self.places)))
        for line in allLines :
            words = line.split()
            self.data[self.users[words[0]]][self.places[words[1]]] = 1


