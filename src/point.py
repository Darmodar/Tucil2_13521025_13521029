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

def bruteforce(matriksofPoint):
    minDistance = calculateDistance(matriksofPoint[0], matriksofPoint[1])
    for i in range(len(matriksofPoint)):
        for j in range(i+1, len(matriksofPoint)):
            if calculateDistance(matriksofPoint[i], matriksofPoint[j]) <= minDistance:
                minDistance = calculateDistance(matriksofPoint[i], matriksofPoint[j])
                point1 = matriksofPoint[i]
                point2 = matriksofPoint[j]

    return minDistance, point1, point2

def divideAndConquer(matriksofPoint):
    print(matriksofPoint)
    if len(matriksofPoint) == 3:
        return bruteforce(matriksofPoint)
    elif len(matriksofPoint) == 2:
        return calculateDistance(matriksofPoint[0], matriksofPoint[1]), matriksofPoint[0], matriksofPoint[1]
    else:
        if len(matriksofPoint) % 2 == 0:
            mid = len(matriksofPoint) // 2
            left = matriksofPoint[:mid]
            right = matriksofPoint[mid:]
            leftmin = divideAndConquer(left)
            rightmin = divideAndConquer(right)
            if leftmin[0] <= rightmin[0]:
                return leftmin
            else:
                return rightmin

        else:
            mid = len(matriksofPoint) // 2
            left = matriksofPoint[:mid]
            right = matriksofPoint[mid+1:]
            leftmin = divideAndConquer(left)
            rightmin = divideAndConquer(right)
            if leftmin[0] <= rightmin[0]:
                distance, p1, p2 = leftmin
            else:
                distance, p1, p2 = rightmin
            
            # mengecek jika terdapat point yang berada dalam jarak mid + distance
            inMid = []
            for point in matriksofPoint:
                if abs(point[0] - matriksofPoint[mid][0]) < distance:
                    inMid.append(point)
            # sorting array of point yang berada dalam jangkauan distance
            inMid = sorted(inMid, key=lambda p: p[1])
            # mencari dua poin yang jaraknya kurang dari distance
            for i in range(len(inMid)):
                for j in range(i+1, len(inMid)):
                    d = calculateDistance(inMid[i], inMid[j])
                    if d < distance:
                        p1, p2 = inMid[i], inMid[j]
                        distance = d
    
            return (distance, p1, p2)

         



