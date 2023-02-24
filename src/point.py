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
    return ((point1.X-point2.X)**2 + (point1.Y-point2.Y)**2 + (point1.Z-point2.Z)**2)**(1/2)

def bruteforce(matriksofPoint):
    minDistance = calculateDistance(matriksofPoint[0], matriksofPoint[1])
    for i in range(len(matriksofPoint)):
        for j in range(i+1, len(matriksofPoint)):
            if calculateDistance(matriksofPoint[i], matriksofPoint[j]) <= minDistance:
                minDistance = calculateDistance(matriksofPoint[i], matriksofPoint[j])
    return minDistance

def divideAndConquer(matriksofPoint):
    if len(matriksofPoint) <= 3:
        return bruteforce(matriksofPoint)
    else:
        mid = len(matriksofPoint)//2
        left = matriksofPoint[:mid]
        right = matriksofPoint[mid:]
        minDistance = min(divideAndConquer(left), divideAndConquer(right))
        return minDistance



