from point import *
import time

def bruteforce(matriksofPoint):
    global countBF
    global timeBF
    countBF = 0
    startTime = time.time()
    minDistance = calculateDistance(matriksofPoint[0], matriksofPoint[1])
    countBF += 1
    for i in range(len(matriksofPoint)):
        for j in range(i+1, len(matriksofPoint)):
            countBF += 1
            if calculateDistance(matriksofPoint[i], matriksofPoint[j]) <= minDistance:
                minDistance = calculateDistance(matriksofPoint[i], matriksofPoint[j])
                countBF += 1
                point1 = matriksofPoint[i]
                point2 = matriksofPoint[j]
    endTime = time.time()
    timeBF = endTime - startTime
    return minDistance, point1, point2

def divideAndConquer(matriksofPoint):
    global countDaC
    global timeDaC
    countDaC = 0
    startTime = time.time()
    if len(matriksofPoint) == 3:
        endTime = time.time()
        timeDaC = endTime - startTime
        res = bruteforce(matriksofPoint)
        countDaC += countBF
        return res
    elif len(matriksofPoint) == 2:
        endTime = time.time()
        timeDaC = endTime - startTime
        countDaC += 1
        return calculateDistance(matriksofPoint[0], matriksofPoint[1]), matriksofPoint[0], matriksofPoint[1]
    else:
        if len(matriksofPoint) % 2 == 0:
            mid = len(matriksofPoint) // 2
            left = matriksofPoint[:mid]
            right = matriksofPoint[mid:]
            leftmin = divideAndConquer(left)
            rightmin = divideAndConquer(right)
            if leftmin[0] <= rightmin[0]:
                distance, p1, p2 = leftmin
            else:
                distance, p1, p2 = rightmin
            xMid = matriksofPoint[0][0] + (abs(matriksofPoint[0][0] - matriksofPoint[-1][0]))/2
            # mengecek jika terdapat point yang berada dalam jarak mid + distance
            inMid = []
            for point in matriksofPoint:
                if abs(point[0] - xMid) < distance:
                    inMid.append(point)
            # sorting array of point yang berada dalam jangkauan distance berdasarkan koordinat-y
            inMid = sorted(inMid, key=lambda p: p[1])
            # mencari dua poin yang jaraknya kurang dari distance
            for i in range(len(inMid)):
                for j in range(i+1, len(inMid)):
                    d = calculateDistance(inMid[i], inMid[j])
                    if d < distance:
                        p1, p2 = inMid[i], inMid[j]
                        distance = d
            endTime = time.time()
            timeDaC = endTime - startTime
            return (distance, p1, p2)

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
            xMid = matriksofPoint[0][0] + (abs(matriksofPoint[0][0] - matriksofPoint[-1][0]))/2
            # mengecek jika terdapat point yang berada dalam jarak mid + distance
            inMid = []
            for point in matriksofPoint:
                if abs(point[0] - xMid) < distance:
                    inMid.append(point)
            # sorting array of point yang berada dalam jangkauan distance berdasar koordinat-y
            inMid = sorted(inMid, key=lambda p: p[1])
            # mencari dua poin yang jaraknya kurang dari distance
            for i in range(len(inMid)):
                for j in range(i+1, len(inMid)):
                    d = calculateDistance(inMid[i], inMid[j])
                    if d < distance:
                        p1, p2 = inMid[i], inMid[j]
                        distance = d
            endTime = time.time()
            timeDaC = endTime - startTime
            return (distance, p1, p2)

def getTimeBF():
    return timeBF

def getTimeDaC():
    return timeDaC

def getNOperationBF():
    return countBF

def getNOperationDaC():
    return countDaC