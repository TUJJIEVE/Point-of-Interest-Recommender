
import numpy as np 



class CollaborativeFiltering :

    def __init__(self ,k):
        self.k = k
        self.CulM = None
        self.locSet = {}
        self.usrSet = {}
        self.simW = None
        self.trainFile= ""
        
    def getLocationSetAndUserSet(self):
        inputFile = None
        inputFile = open(self.trainFile,"r")
        if inputFile == None :
            return False
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
        # return locationSet , userSet ;
        self.locSet = locationSet 
        self.usrSet = userSet 
        return True 

        # CulMatrix  is user x locations
        def getCulMatrix(self):
            lSet = self.locSet
            uSet = self.usrSet
            inputFile = None 
            inputFile = open(self.trainFile,"r")
            if inputFile == None :
                return False
            matrix = np.zeros((len(uSet),len(lSet)))
            print("size =",len(matrix) , len(matrix[0]))
            allLines = inputFile.readlines()
            for line in allLines:
                words = line.split()
                usrIdx = uSet[words[0]]
                _,_,locIdx = lSet[words[1]]
                matrix[usrIdx][locIdx] = 1 
            # print(matrix)
            self.CulM = matrix
            return True

        def getWuvMatrix(self) :
            matrix = self.CulM
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
            self.simW = res
            return True

        def getSortedIndexs( weights ):
            sortedIndexs = sorted(range(len(weights)),key=lambda k : weights[k])
            return sortedIndexs



        def learn(self , fileName):
            self.trainFile = fileName 
            self.getLocationSetAndUserSet()
            self.getCulMatrix()
            self.getWuvMatrix()
            if self.simW == None or self.CulM == None :
                return False
            return True

       
        def predictPlaces( self  , userIds ) :
            if self.simW == None :
                return None
            predictedPlaces = []
            similarityMatrix = self.simW
            ULmatrix = self.CulM
            k = self.k 
            for i in userIds :
                i = self.usrSet[i]
                userWeightwrtUserindex = getSortedIndexs(similarityMatrix[userIds]) #gets sorted indexs in asending order
                bestK_SimilarUsers = userWeightwrtUserindex[len(userWeightwrtUserindex)-k:] #picks last k indexs 
                predictedProb = []
                for locInd in range(len(similarityMatrix[0])) :
                    num = 0.0000000001
                    den = 0.0000000001 #added only not to make it divisible by zero condition
                    for x in bestK_SimilarUsers :
                        num += userWeightwrtUserindex[x] * ULmatrix[x][locInd]
                        den += userWeightwrtUserindex[x] 
                    predictedProb.append(num/den)
                predictPlaces.append(predictedProb)
            return predictPlaces