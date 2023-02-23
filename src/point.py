import random

class point:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z

    def randomPoint(numberOfPoint):
        ArrayOfpoint = []
        for i in range(numberOfPoint):
            temp = point(0,0,0)
            random_number = random.randint(0, 1000)
            temp.X = random_number
            random_number = random.randint(0, 1000)
            temp.Y = random_number
            random_number = random.randint(0, 1000)
            temp.Z = random_number
            ArrayOfpoint.append(temp)
        return ArrayOfpoint
    
    def sortPoint(arrayOfP):
        return sorted(arrayOfP, key=lambda x: x.X)
    
    def __str__(self):
        return f"({self.X},{self.Y},{self.Z})"

