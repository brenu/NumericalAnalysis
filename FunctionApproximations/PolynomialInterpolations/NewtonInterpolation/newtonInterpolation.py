from scipy.interpolate import make_interp_spline
from sympy import lambdify, Symbol, parse_expr, simplify
import numpy as np
import matplotlib.pyplot as plt
import re

outputFile = open("result.txt", "w")
outputFile.close()

def dividedValues(points):
    pointsLength = len(points)
    coefficients = np.zeros([pointsLength, pointsLength])

    coefficients[:,0] = points[:,1]
    
    for j in range(1,pointsLength):
        for i in range(pointsLength-j):
            coefficients[i][j] = \
           (coefficients[i+1][j-1] - coefficients[i][j-1]) / (points[i+j][0]-points[i][0])
            
    return coefficients

def newton(coefficients, points):
    polynome = "{}".format(coefficients[0][0])

    pointsLength = len(points)

    for i in range(1,pointsLength):
        mainOperator = " + " if coefficients[0][i] >= 0 else " - "
        polynome = polynome + " {} ({}".format(mainOperator, abs(coefficients[0][i]))
        for j in range(0,i):
            mainOperator = " - " if points[j][0] >= 0 else " + "
            polynome = polynome + " * (x {} {})".format(mainOperator, abs(points[j][0]))
        polynome = polynome + ")"

    return str(simplify(polynome))


def main():
    inputFile = open("input.txt", "r")

    for lineIndex, line in enumerate(inputFile):
        line = re.sub('[\n]*','',line)
        line = line.split(";")
        
        arrayPoints = []

        for pointString in line:
            arrayPoints.append(np.array(pointString.replace('[', '').replace(']','').replace('\n', '').split(',')).astype(np.float))

        points = np.array(arrayPoints)

        polynomeString = newton(dividedValues(points), points)
        polynome = lambdify(Symbol('x'), parse_expr(polynomeString))

        xValues = []
        yValues = []
        predictedValues = []

        for i in range(len(points)):
            xValues.append(points[i][0])
            yValues.append(points[i][1])
            predictedValues.append(polynome(points[i][0]))

        outputFile = open("result.txt", "a")
        outputFile.write("---------------Problem Nº {}-------------------\n".format(lineIndex+1))
        outputFile.write("Approximate equation found: Y = {}".format(polynomeString))
        outputFile.write("\n\n")
        outputFile.close()

        if len(predictedValues) > 3:
            newXValues = np.linspace(min(xValues), max(xValues), 200)
            spline = make_interp_spline(xValues, predictedValues, k=3)
            smoothYValues = spline(newXValues)


            plt.scatter(xValues, yValues)
            plt.plot(newXValues, smoothYValues, color='blue')
            plt.show()
        else:
            plt.scatter(xValues, yValues)
            plt.plot(xValues, predictedValues, color='blue')
            plt.show()

main()