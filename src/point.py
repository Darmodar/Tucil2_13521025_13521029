import random

def randomPoint(numberOfPoint, dimension):
    matriksOfpoint = [[]]
    for i in range(numberOfPoint):
        for j in range(dimension):
            matriksOfpoint[i][j] = random.randint(0,1000)
        
    return matriksOfpoint

def sortPoint(matriksofPoint):
    return matriksofPoint[matriksofPoint[:, 1].argsort()]

def calculateDistance(point1, point2):
    return ((point1.X-point2.X)**2 + (point1.Y-point2.Y)**2 + (point1.Z-point2.Z)**2)**(1/2)



