from sympy import *

def main():
    inputFile = open('input.txt', 'r') 

    outputFile = open('result.txt', 'w')
    outputFile.write("Results considering ε = 10⁻²\n\n\n")
    outputFile.close()

    for index, line in enumerate(inputFile):
        items = line.split(",")
        a = float(items[1])
        b = float(items[2])
        x = Symbol('x') 

        evaluatedExpression = lambdify(x, parse_expr(items[0]))

        expressionZero = 0
        temporaryX = 1
        attempts = 0

        while evaluatedExpression(temporaryX) >= 0.01 or evaluatedExpression(temporaryX) <= -0.01:
            attempts = attempts + 1
            if attempts <= 10000:
                fa = evaluatedExpression(a)
                fb = evaluatedExpression(b)
                temporaryX = (a * fb - b * fa) / (fb - fa)
                result = evaluatedExpression(temporaryX)

                if result <= -0.01  or result >= 0.01:
                    if result*fa < 0:
                        b = temporaryX
                    else:
                        a = temporaryX
                else:
                    outputFile = open('result.txt', 'a')
                    outputFile.write("-------------------- Equation {} --------------------\n".format(index))
                    outputFile.write("Considering the interval [{}, {}]\n".format(float(items[1]), float(items[2])))
                    outputFile.write("{} => {}\n\n\n".format(items[0], temporaryX))
                    outputFile.close()
                    break
            else:
                outputFile = open('result.txt', 'a')
                outputFile.write("-------------------- Equation {} --------------------\n".format(index))
                outputFile.write("Considering the interval [{}, {}]\n".format(float(items[1]), float(items[2])))
                outputFile.write("{} => Unable to find approximate root, last was {} => {}\n\n\n".format(items[0], temporaryX, evaluatedExpression(temporaryX)))
                outputFile.close()
                break
    
main()
print("Done. See the results on result.txt")