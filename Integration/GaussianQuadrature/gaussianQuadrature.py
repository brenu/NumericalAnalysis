from sympy import lambdify, Symbol, parse_expr
import re

outputFile = open("result.txt", "w")
outputFile.close()

def main():
    inputFile = open("input.txt", "r")

    for lineIndex, line in enumerate(inputFile):
        line = line.replace("\n","").split(";")

        originalExpression = line[0]
        aValue = float(line[1])
        bValue = float(line[2])

        parsedExpression = re.sub("(?<![a-zA-Z])x(?![a-zA-Z])","((({} - ({})) * x + ({} - ({})))/2)".format(bValue,aValue,bValue,aValue),originalExpression)

        parsedExpression = "{} * ({})".format((bValue-aValue/2), parsedExpression)

        parsedExpression = lambdify(Symbol('x'), parse_expr(parsedExpression))

        result = 0.1713245 * parsedExpression(-0.932469514) + 0.3607616 * parsedExpression(-0.661209386) \
            + 0.4679139 * parsedExpression(-0.238619186) + 0.4679139 * parsedExpression(0.238619186) \
            + 0.3607616 * parsedExpression(0.661209386) + 0.1713245 * parsedExpression(0.932469514)

        outputFile = open("result.txt", "a")
        outputFile.write("---------------Problem Nº {}-------------------\n".format(lineIndex+1))
        outputFile.write("Calculating the integral of {} between {} and {}:\n".format(originalExpression, aValue, bValue))
        outputFile.write("Approximate value found for 1,2 and 4 segments: {}\n".format(result))
        outputFile.write("\n\n")
        outputFile.close()

main()