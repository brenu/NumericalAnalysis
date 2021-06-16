from sympy import lambdify, Symbol, parse_expr
import numpy as np
import re

outputFile = open("result.txt", "w")
outputFile.close()

def getOperationMultiplier(operationType, index):
    if operationType == "1/3":
        return 4 if index % 2 == 0 else 2
    elif operationType == "3/8":
        return 2 if index % 3 == 0 else 3
    else:
        return 0


def main():
    inputFile = open("input.txt", "r")

    for lineIndex, line in enumerate(inputFile):
        line = line.replace("\n","").split(";")

        originalExpression = line[0]
        expression = lambdify(Symbol('x'), parse_expr(line[0]))
        initialX = float(line[1])
        finalX = float(line[2])
        trapezoidsQuantity = float(line[3])
        
        operationType = line[4]

        h = (finalX - initialX)/trapezoidsQuantity

        if operationType == "1/3":
            multiplier = ((h)/3)
        elif operationType == "3/8":
            multiplier = ((3*h)/8)

        integralResult = 0
        
        for xIndex, x in enumerate(np.arange(initialX, finalX+h, h)):
            if xIndex == 0 or xIndex == trapezoidsQuantity:
                integralResult = integralResult + expression(x)
            else:
                times = getOperationMultiplier(operationType, xIndex)
                integralResult = integralResult + (times * expression(x))

        integralResult = integralResult * multiplier

        outputFile = open("result.txt", "a")
        outputFile.write("---------------Problem Nº {}-------------------\n".format(lineIndex+1))
        outputFile.write("Calculating the integral of {} between {} and {}:\n".format(originalExpression, initialX, finalX))
        outputFile.write("Approximate value found for {} divisions: {}\n".format(trapezoidsQuantity, integralResult))
        outputFile.write("\n\n")
        outputFile.close()
        
        

main()