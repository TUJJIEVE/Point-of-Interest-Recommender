# creates additional files with joining items of same timeslot to same file

def createSeperateFiles(originalFilename , numberofTimeSlots) :
    inputFile = open(originalFilename , "r") 
    outputFiles = []

    for i in range(numberofTimeSlots):
        outputFiles.append(open(originalFilename+str(i),"w"))
    
    alllines = inputFile.readlines()
    for line in alllines :
        words = line.split()
        outputFiles[int(words[3])].write(line+"\n")
    
    for x in outputFiles :
        x.close()
    

createSeperateFiles("modified",24)
