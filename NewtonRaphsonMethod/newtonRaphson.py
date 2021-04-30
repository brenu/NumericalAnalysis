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

        expression = parse_expr(items[0])
        expression_prime = expression.diff(x)

        expression = lambdify(x, expression)
        expression_prime = lambdify(x, expression_prime)
        
        temporaryX =  (b + a) / 2

        attempts = 0
        while attempts < 10000:
            attempts = attempts + 1
            result = expression(temporaryX)

            if result >= -0.01 and result <= 0.01:
                outputFile = open('result.txt', 'a')
                outputFile.write("-------------------- Equation {} --------------------\n".format(index))
                outputFile.write("Considering the interval [{}, {}]\n".format(a, b))
                outputFile.write("{} => {}\n\n\n".format(items[0], temporaryX))
                outputFile.close()
                break
            
            temporaryX = temporaryX - (expression(temporaryX) / expression_prime(temporaryX))

        if attempts >= 10000:
            outputFile = open('result.txt', 'a')
            outputFile.write("-------------------- Equation {} --------------------\n".format(index))
            outputFile.write("Considering the interval [{}, {}]\n".format(a, b))
            outputFile.write("{} => Unable to find approximate root\n\n\n".format(items[0]))
            outputFile.close()

    inputFile.close()

main()
print("Done. See the results on result.txt")

        

            
        