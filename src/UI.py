from Plotting import *
from getSpec import *
from solver import *

def getNPoints():
    n = int(input("Please enter the number of points:\n  > "))
    return n

def getDimension():
    d = int(input("Enter the dimension:\n  > "))
    return d

def plotting(matriksOfPoint, n, result):
    if (len(matriksOfPoint[0])) == 3:
        p = str(input("\nIt seems like the points are built on 3D, do you want to plot the points? (y/n)\n  > "))
        if p == "y":
            plot3D(matriksOfPoint, n, result)
    else:
        print("Your points are not built on 3D, we couldn't provide the graph")
        

def exit():
    print("Thank you for using our program ^v^")
    print("I hope u have a great day")
    input()

def asciiart():
    print("""                         
              ////////          
        ////////&@///////,     
    (///////%%&///////%,#/////// 
    //#//#//////#*////////////, .
    /////((////%////(////(..,..  
    /(//////((,//////( .    ... .          Pair of Closest Points solver
    (///%*//(////#     .   *, ...
    #//////#*///(    .,. .  ... 
    ///#////////( .... ... *....
    //(///%////(...../.........
        (/////#/(...........    
            (////(.......        
                (/(...  
    """)

def program():
    asciiart()
    n = getNPoints()
    dim = getDimension()
    matrixOfPoints = randomPoint(n, dim)
    matrixOfPoints = sortPoint(matrixOfPoints)
    print("Random points generated, preview:")
    viewPoints(matrixOfPoints)
    resBF = bruteforce(matrixOfPoints)
    print("\nClosest pair using Bruteforce algorithm found! Here's the result:")
    print("  Distance between the two:", resBF[0])
    print("  Point 1:", resBF[1])
    print("  Point 2:", resBF[2])
    print("  Number of operations executed:", getNOperationBF())
    print("  Elapsed time:", round(getTimeBF(), ndigits=2), "second(s)")
    resDaC = divideAndConquer(matrixOfPoints)
    print("\nClosest pair using Divide and Conquer algorithm found! Here's the result:")
    print("  Distance between the two:", resDaC[0])
    print("  Point 1:", resDaC[1])
    print("  Point 2:", resDaC[2])
    print("  Number of operations executed:", getNOperationDaC())
    print("  Elapsed time:", round(getTimeDaC(), ndigits=2), "second(s)")
    print("\nAbove results are obtained using your PC specification below:")
    getPCSpec()
    plotting(matrixOfPoints, n, resDaC)
    exit()
