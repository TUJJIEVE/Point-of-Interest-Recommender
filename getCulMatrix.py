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

# CulMatrix  is user x locations
def getCulMatrix(fileName , locSet , usrSet):
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

#similarity matrix is weight matrix  i.e user x user matrix 
#similarity array is row from similarity matrix that we have taken
# k is the tweek factor #i.e number of similar users it has to consider 
# userIndexs
def predictPlaces( userIndexs , similarityMatrix  , ULmatrix , k ) :
    predictedPlaces = []
    for i in userIndexs :
        userWeightwrtUserindex = similarityMatrix[userIndexs] 
        # sort(userWeightwrtUserindex)
        bestK_SimilarUsers = userWeightwrtUserindex[:k] #NEED TO WRITE A FUNCTION TO MAP INDEXS 
        predictedProb = []
        for locInd in range(len(similarityMatrix[0])) :
            num = 0.0000000001
            den = 0.0000000001 #added only not to make it divisible by zero condition
            for x in bestK_SimilarUsers :
                num += userWeightwrtUserindex[x] * CulMatrix[x][locInd]
                den += userWeightwrtUserindex[x] 
            predictedProb.append(num/den)
        predictPlaces.append(predictedProb)
    return predictPlaces




fileName = "modified"
locSet , usrSet = getLocationSetAndUserSet(fileName)
CulMatrix = getCulMatrix("fileName",locSet,usrSet) 
WuvMatrix = getWuvMatrix(CulMatrix)

print(WuvMatrix)