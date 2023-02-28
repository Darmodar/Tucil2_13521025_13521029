import random

def randomPoint(numberOfPoint, dimension):
    matriksOfpoint = [[0 for _ in range(dimension)] for _ in range(numberOfPoint)]
    for i in range(numberOfPoint):
        for j in range(dimension):
            matriksOfpoint[i][j] = random.randint(0,1000)
        
    return matriksOfpoint

def sortPoint(matriksofPoint):
    return sorted(matriksofPoint, key=lambda a_entry: a_entry[0]) 

def calculateDistance(point1, point2):
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i])**2
    return sum**(1/2)

def viewPoints(matrixOfPoints):
    if (len(matrixOfPoints) > 5):
        for i in range(5):
            print(matrixOfPoints[i], end=' ')
        print("...")
    else:
        print(matrixOfPoints)