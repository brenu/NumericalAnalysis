from sympy import lambdify, Symbol, parse_expr, symbols
import numpy as np
import matplotlib.pyplot as plt

outputFile = open("result.txt", "w")
outputFile.close()

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
        firstGuess = float(line[7])
        secondGuess = float(line[8])
        
        h = l / 12 # Dividindo em 5 mil pontos

        f1 = lambdify((x,y,z),"z")
        
        f2 = lambdify((x,y,z),"{} * (y - {})".format(hLine,tA))
        
        values = [[0, t1]]
        zValues = [[0,firstGuess]]

        for xIndex, xValue in enumerate(np.arange(x0+h, l+h/2, h)):
            k1 = h*f1(xValue,values[xIndex][1],zValues[xIndex][1])
            l1 = h*f2(xValue,values[xIndex][1],zValues[xIndex][1])
            k2 = h*f1(xValue+h/2,values[xIndex][1]+k1/2,zValues[xIndex][1]+l1/2)
            l2 = h*f2(xValue+h/2,values[xIndex][1]+k1/2,zValues[xIndex][1]+l1/2)
            k3 = h*f1(xValue+h/2,values[xIndex][1]+k2/2,zValues[xIndex][1]+l2/2)
            l3 = h*f2(xValue+h/2,values[xIndex][1]+k2/2,zValues[xIndex][1]+l2/2)
            k4 = h*f1(xValue+h,values[xIndex][1]+k3,zValues[xIndex][1]+l3)
            l4 = h*f2(xValue+h,values[xIndex][1]+k3,zValues[xIndex][1]+l3)

            yN = values[xIndex][1]+(k1+2*k2+2*k3+k4)/6
            zN = zValues[xIndex][1]+(l1+2*l2+2*l3+l4)/6

            values.append([xValue, yN])
            zValues.append([xValue, zN])

        firstResponse = values[-1][1]
        values = [[0, t1]]
        zValues = [[0,secondGuess]]

        for xIndex, xValue in enumerate(np.arange(x0+h, l+h/2, h)):
            k1 = h*f1(xValue,values[xIndex][1],zValues[xIndex][1])
            l1 = h*f2(xValue,values[xIndex][1],zValues[xIndex][1])
            k2 = h*f1(xValue+h/2,values[xIndex][1]+k1/2,zValues[xIndex][1]+l1/2)
            l2 = h*f2(xValue+h/2,values[xIndex][1]+k1/2,zValues[xIndex][1]+l1/2)
            k3 = h*f1(xValue+h/2,values[xIndex][1]+k2/2,zValues[xIndex][1]+l2/2)
            l3 = h*f2(xValue+h/2,values[xIndex][1]+k2/2,zValues[xIndex][1]+l2/2)
            k4 = h*f1(xValue+h,values[xIndex][1]+k3,zValues[xIndex][1]+l3)
            l4 = h*f2(xValue+h,values[xIndex][1]+k3,zValues[xIndex][1]+l3)

            yN = values[xIndex][1]+(k1+2*k2+2*k3+k4)/6
            zN = zValues[xIndex][1]+(l1+2*l2+2*l3+l4)/6

            values.append([xValue, yN])
            zValues.append([xValue, zN])

        secondResponse = values[-1][1]

        z0 = firstGuess + ((secondGuess - firstGuess)/(secondResponse-firstResponse))*(t2-firstResponse)
        
        outputFile = open("result.txt", "a")
        outputFile.write("---------------Problem Nº {}-------------------\n".format(lineIndex+1))
        outputFile.write("Calculating Z(0) for {} between {} and {} with h = {}:\n".format(originalExpression,x0,l,h))
        outputFile.write("Result found: {}\n".format(z0))
        outputFile.write("\n\n")
        outputFile.close()

        zValues = [[0, z0]]
        values = [[0, t1]]
        xValues = []
        yValues = []

        for xIndex, xValue in enumerate(np.arange(x0+h, l+h/2, h)):
            k1 = h*f1(xValue,values[xIndex][1],zValues[xIndex][1])
            l1 = h*f2(xValue,values[xIndex][1],zValues[xIndex][1])
            k2 = h*f1(xValue+h/2,values[xIndex][1]+k1/2,zValues[xIndex][1]+l1/2)
            l2 = h*f2(xValue+h/2,values[xIndex][1]+k1/2,zValues[xIndex][1]+l1/2)
            k3 = h*f1(xValue+h/2,values[xIndex][1]+k2/2,zValues[xIndex][1]+l2/2)
            l3 = h*f2(xValue+h/2,values[xIndex][1]+k2/2,zValues[xIndex][1]+l2/2)
            k4 = h*f1(xValue+h,values[xIndex][1]+k3,zValues[xIndex][1]+l3)
            l4 = h*f2(xValue+h,values[xIndex][1]+k3,zValues[xIndex][1]+l3)

            yN = values[xIndex][1]+(k1+2*k2+2*k3+k4)/6
            zN = zValues[xIndex][1]+(l1+2*l2+2*l3+l4)/6

            values.append([xValue,yN])
            zValues.append([xValue, zN])

            xValues.append(xValue)
            yValues.append(yN)

        plt.scatter([l], [t2], color='orange')
        plt.plot(xValues, yValues, color='blue')
        plt.show()


main()