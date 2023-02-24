from point import *
# Develop
n = int(input("Masukkan nilai N!\n"))
dimensi = int(input("Masukkan nilai dimensi!\n"))
point = randomPoint(n, dimensi)
point = sortPoint(point)
print(divideAndConquer(point))
