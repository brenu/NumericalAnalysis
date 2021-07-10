from sympy import lambdify, Symbol, parse_expr, symbols
import numpy as np
import matplotlib.pyplot as plt

outputFile = open("result.txt", "w")
outputFile.close()

def main():
    inputFile = open("input.txt", "r")

    x, y = symbols("x y")

    for lineIndex, line in enumerate(inputFile):
        line = line.replace("\n","").split(";")

        originalExpression = line[0]
        expression = lambdify((x,y),originalExpression)
        a = float(line[2])
        b = float(line[3])
        h = float(line[4])

        values = [[a, float(line[1])]]

        for xIndex, xValue in enumerate(np.arange(a+h, b+h/2, h)):
            k1 = expression(values[xIndex][0],values[xIndex][1])
            k2 = expression((values[xIndex][0]+(3*h/4)),(values[xIndex][1]+(3*h*k1)/4))
            yValue = values[xIndex][1] + (k1/3 + 2*k2/3)*h

            values.append([xValue, yValue])
        
        outputFile = open("result.txt", "a")
        outputFile.write("---------------Problem Nº {}-------------------\n".format(lineIndex+1))
        outputFile.write("Calculating the points of {} between {} and {} with h = {}:\n".format(originalExpression,a,b,h))
        outputFile.write("Results found: {}\n".format(values))
        outputFile.write("\n\n")
        outputFile.close()

        xValues = []
        yValues = []

        for value in values:
            xValues.append(value[0])
            yValues.append(value[1])

        plt.scatter(xValues, yValues)
        plt.plot(xValues, yValues, color='blue')
        plt.show()

main()