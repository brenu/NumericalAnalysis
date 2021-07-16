from sympy import lambdify, Symbol, parse_expr, symbols
import numpy as np
import matplotlib.pyplot as plt
import copy

outputFile = open("result.txt", "w")
outputFile.close()

def gaussSeidel(matrix, extension):
    matrixLength = len(matrix)

    x0 = [0] * matrixLength
    x = copy.deepcopy(x0) 
    counter = 0

    while counter < 10000:
        for i in range(matrixLength):
            cellsSum = 0
            for j in range(0, i):
                cellsSum = cellsSum + matrix[i][j] * x0[j] / matrix[i][i]
            for j in range(i+1,matrixLength):    
                cellsSum = cellsSum + matrix[i][j] * x0[j] / matrix[i][i]
            x[i] = (extension[i]/matrix[i][i]) - cellsSum
        if abs(safe_norm(x) - safe_norm(x0)) < 0.01:
            break
        else:
            x0 = copy.deepcopy(x)
        counter = counter + 1

    return x0

def safe_norm(x):
    return np.linalg.norm(np.matrix(x))  

def main():
    inputFile = open("input.txt", "r")

    x, y, z = symbols("x y z")

    for lineIndex, line in enumerate(inputFile):
        line = line.replace("\n","").split(";")

        originalExpression = line[0]
        x0 = float(line[1])
        l = float(line[2])
        tA = float(line[3])
        t1 = float(line[4])
        t2 = float(line[5])
        hLine = float(line[6])

        deltaX = 10 # 4 intern points
        h = (l - x0) / (deltaX-1)

        fdExpressionOne = 2+hLine*deltaX
        fdExpressionTwo = hLine*deltaX*tA

        matrix = np.zeros((deltaX,deltaX))
        matrixResults = np.zeros((deltaX))

        matrix[0][0] = fdExpressionOne
        matrix[0][1] = -1
        matrix[-1][-1] = fdExpressionOne
        matrix[-1][-2] = -1

        for xIndex, xValue in enumerate(np.arange(x0, l+h/2, h)):
            if xValue != x0 and xValue != l:
                    matrix[xIndex][xIndex] = fdExpressionOne
                    matrix[xIndex][xIndex - 1] = -1
                    matrix[xIndex][xIndex + 1] = -1
                    
                    matrixResults[xIndex] = fdExpressionTwo
            else:
                if xValue == x0:
                    matrixResults[xIndex] = fdExpressionTwo + t1
                else:
                    matrixResults[xIndex] = fdExpressionTwo + t2
        
        result = gaussSeidel(matrix, matrixResults)

        outputFile = open("result.txt", "a")
        outputFile.write("---------------Problem Nº {}-------------------\n".format(lineIndex+1))
        outputFile.write("Calculating points for {} between {} and {} with h = {}:\n".format(originalExpression,x0,l,h))
        outputFile.write("Results found (only inner values): {}\n".format(result))
        outputFile.write("\n\n")
        outputFile.close()

        h = (l - x0) / (deltaX+1)

        xValues = np.arange(x0, l+h/2, h)
        yValues = [t1,*result,t2]
        print(xValues,yValues)

        plt.scatter([xValues], [yValues], color='orange')
        plt.plot(xValues, yValues, color='blue')
        plt.show()

main()