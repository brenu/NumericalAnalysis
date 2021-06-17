from sympy import lambdify, Symbol, parse_expr
import numpy as np
import re

outputFile = open("result.txt", "w")
outputFile.close()

def trapezoids(initialX, finalX, expression, segments):
    integralResult = 0

    h = (finalX - initialX)/segments

    for xIndex, x in enumerate(np.arange(initialX, finalX+h, h)):
        if xIndex == 0 or xIndex == segments+1:
            integralResult = integralResult + expression(x)
        else:
            integralResult = integralResult + (2 * expression(x))

    integralResult = integralResult * (h/2)

    return integralResult

def main():
    inputFile = open("input.txt", "r")

    for lineIndex, line in enumerate(inputFile):
        line = line.replace("\n","").split(";")

        originalExpression = line[0]

        expression = lambdify(Symbol('x'), parse_expr(line[0]))
        initialX = float(line[1])
        finalX = float(line[2])

        integrals = [[],[],[]]
        segments = 1
     
        for i in range(3):
            integrals[i].append(trapezoids(initialX, finalX, expression, segments))
            segments = segments * 2
        
        for i in range(2):
            integrals[i].append((4/3) * integrals[i+1][0] - (1/3)*integrals[i][0])

        integrals[0].append((16/15) * integrals[1][1] - (1/15) * integrals[0][1])

        integralResult = integrals[0][2]

        outputFile = open("result.txt", "a")
        outputFile.write("---------------Problem Nº {}-------------------\n".format(lineIndex+1))
        outputFile.write("Calculating the integral of {} between {} and {}:\n".format(originalExpression, initialX, finalX))
        outputFile.write("Approximate value found for 1,2 and 4 segments: {}\n".format(integralResult))
        outputFile.write("\n\n")
        outputFile.close()
        
        

main()