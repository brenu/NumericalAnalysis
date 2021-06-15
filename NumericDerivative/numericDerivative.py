from scipy.interpolate import make_interp_spline
from sympy import lambdify, Symbol, parse_expr, simplify
import numpy as np
import matplotlib.pyplot as plt
import re
import copy

outputFile = open("result.txt", "w")
outputFile.close()

def firstOrder(expression, xValue, delta):
    expressionOne = expression.replace("x", "(x + {})".format(delta))
    expressionTwo = expression.replace("x", "(x - {})".format(delta))

    deltasDistance = (xValue + delta) - (xValue - delta)

    derivativeString = "(({}) - ({}))/({})".format(expressionOne, expressionTwo,deltasDistance)
    
    return derivativeString

def secondOrder(expression, xValue, delta):
    leftExpression = expression.replace("x", "(x + {})".format(delta))
    rightExpression = expression.replace("x", "(x - {})".format(delta))

    deltasDistance = delta*delta

    derivativeString = "(({}) - (2*({})) + ({}))/({})".format(leftExpression, expression, rightExpression, deltasDistance)

    return derivativeString


def main():
    inputFile = open("input.txt", "r")

    for lineIndex, line in enumerate(inputFile):
        line = line.replace("\n","").split(";")

        originalEquation = line[0]
        xValue = line[1]
        delta = line[2]
        derivativeOrder = line[3]

        if derivativeOrder == '1':
            derivativeString = firstOrder(originalEquation, float(xValue), float(delta))
        else:
            derivativeString = secondOrder(originalEquation, float(xValue), float(delta))

        derivative = lambdify(Symbol('x'), parse_expr(derivativeString))

        outputFile = open("result.txt", "a")
        outputFile.write("---------------Problem Nº {}-------------------\n".format(lineIndex+1))
        derivativeSymbol = "f'" if derivativeOrder == '1' else "f''"
        outputFile.write("Approximate derivative found: {}(x) = {} + error(h²)\n".format(derivativeSymbol,simplify(derivativeString)))
        outputFile.write("{}({}) = {}\n".format(derivativeSymbol,xValue, derivative(float(xValue))))
        outputFile.write("\n\n")
        outputFile.close()

        xValues = np.arange(0,1000)
        
        predictedValues = []

        for i in range(0,1000):
            predictedValues.append(round(derivative(xValues[i]),2))

        newXValues = np.linspace(min(xValues), max(xValues), 1000)
        spline = make_interp_spline(xValues, predictedValues, k=3)
        smoothYValues = spline(newXValues)

        plt.plot(newXValues, smoothYValues, color='blue')
        plt.show()
        
main()