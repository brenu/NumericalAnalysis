from sympy import lambdify, Symbol, parse_expr
import numpy as np
import re

outputFile = open("result.txt", "w")
outputFile.close()

def main():
    inputFile = open("input.txt", "r")

    for lineIndex, line in enumerate(inputFile):
        line = line.replace("\n","").split(";")

        originalExpression = line[0]
        expression = lambdify(Symbol('x'), parse_expr(line[0]))
        initialX = float(line[1])
        finalX = float(line[2])
        trapezoidsQuantity = float(line[3])

        h = (finalX - initialX)/trapezoidsQuantity

        integralResult = 0
        
        for xIndex, x in enumerate(np.arange(initialX, finalX+h, h)):
            if xIndex == 0 or xIndex == trapezoidsQuantity+1:
                integralResult = integralResult + expression(x)
            else:
                integralResult = integralResult + (2 * expression(x))

        integralResult = integralResult * (h/2)

        outputFile = open("result.txt", "a")
        outputFile.write("---------------Problem Nº {}-------------------\n".format(lineIndex+1))
        outputFile.write("Calculating the integral of {} between {} and {}:\n".format(originalExpression, initialX, finalX))
        outputFile.write("Approximate value found for {} trapezoids: {}\n".format(trapezoidsQuantity, integralResult))
        outputFile.write("\n\n")
        outputFile.close()
        
        

main()