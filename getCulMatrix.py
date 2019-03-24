#
#   getCulMatrix gives Cu,l i,e is whether a used went to this location of not  
#
import numpy as np 

def getLocationSetAndUserSet(fileName):
    inputFile = open(fileName,"r")
    locationSet = {} #location with coordinates
    userSet = {} #user id with index
    allLines = inputFile.readlines()
    locIndex = 0
    usrIndex = 0 
    for line in allLines :
        words = line.split()
        if words[0] not in userSet :
            userSet[words[0]] = usrIndex 
            usrIndex += 1
        if words[1] not in locationSet :
            point = words[2].split(',')
            locationSet[words[1]] = (float(point[0]),float(point[1]),locIndex)
            locIndex += 1 
    inputFile.close()
    # print(locationSet)
    # print(userSet)
    return locationSet , userSet ;

def getCulMatrix(fileName):
    locSet , usrSet = getLocationSetAndUserSet(fileName)
    inputFile = open(fileName,"r")
    matrix = np.zeros((len(usrSet),len(locSet)))
    print("size =",len(matrix) , len(matrix[0]))
    allLines = inputFile.readlines()
    for line in allLines:
        words = line.split()
        usrIdx = usrSet[words[0]]
        _,_,locIdx = locSet[words[1]]
        matrix[usrIdx][locIdx] = 1 
    print(matrix)
    return matrix
def getWuvMatrix(matrix) :
    nR = len(matrix)
    nC = len(matrix[0])
    res = np.ones((nR,nR))
    i = 0 
    while i < nR :
        j = i+1
        while j < nR :
            print(i,j)
            temp1 = matrix[i,:] * 1
            temp2 = matrix[j,:] * 1
            # print(temp1)
            # print(temp2) 
            # print(temp1*temp2)
            res[i][j] = np.sum(temp1 * temp2) / np.sqrt(np.sum(temp1)*np.sum(temp2))
            # k = 0 
            # numeratoR = 0
            # denom1 = 0
            # denom2 = 0
            # while k < nC :
            #     print(i,j,k)
            #     numeratoR += (matrix[i][k]*matrix[j][k])
            #     denom1 += (matrix[i][k]*matrix[i][k])
            #     denom2 += (matrix[j][k]*matrix[j][k])
            #     k+=1
            # res[i][j] = numeratoR / np.sqrt(denom1 * denom2) ;
            res[j][i] = res[i][j]
            j+=1
        i+=1
    return res 
CulMatrix = getCulMatrix("modified")
WuvMatrix = getWuvMatrix(CulMatrix)
print(WuvMatrix)