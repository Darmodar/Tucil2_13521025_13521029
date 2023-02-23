import random

class point:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z

    def randomPoint(numberOfPoint):
        ArrayOfpoint = []
        temp = point(0,0,0)
        for i in range(numberOfPoint):
            random_number = random.randint(0, 1000)
            temp.X = random_number
            random_number = random.randint(0, 1000)
            temp.Y = random_number
            random_number = random.randint(0, 1000)
            temp.Z = random_number
            ArrayOfpoint.append(temp)
        return ArrayOfpoint
    
    def __str__(self):
        return f"({self.X},{self.Y},{self.Z})"

