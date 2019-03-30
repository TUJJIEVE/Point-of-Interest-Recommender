####
##
#   this file is intended to preprocess the data given into timeslots
##
###


def makeTimeSlots(noSlotsPerDay,filePath):
    noMinsPerslot = 24 * 60 / noSlotsPerDay
    inputFile = open(filePath,"r")
    fileName = "" #get from filePath
    outputFile = open("modified"+fileName,"w")
    allLines = inputFile.readlines()
    for line in allLines:
        words = line.split()
        [a,b] = words[3].split(':')
        
        noOfMins = int(a) * 60 + int(b) 
        print(a,b,noOfMins,noMinsPerslot)
        newLine = words[0]+" "+words[1]+" "+words[2]+" "+str(int(noOfMins / noMinsPerslot))+" "+words[4]
        outputFile.write(newLine)
        outputFile.write("\n")
        print(newLine)
    inputFile.close()
    outputFile.close()



makeTimeSlots(24,"./../poidata/Foursquare/train.txt")
