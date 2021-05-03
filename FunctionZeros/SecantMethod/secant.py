from sympy import *

def main():
    inputFile = open('input.txt', 'r') 

    outputFile = open('result.txt', 'w')
    outputFile.write("Results considering ε = 10⁻²\n\n\n")
    outputFile.close()

    for index, line in enumerate(inputFile):
        items = line.split(",")
        x = Symbol('x') 

        expression = lambdify(x, parse_expr(items[0]))
        
        a = float(items[1])
        b = float(items[2])
        fa = expression(a)
        fb = expression(b)

        if fa >= -0.01 and fa <= 0.01:
            outputFile = open('result.txt', 'a')
            outputFile.write("-------------------- Equation {} --------------------\n".format(index))
            outputFile.write("Considering the interval [{}, {}]\n".format(float(items[1]), float(items[2])))
            outputFile.write("{} => {}\n\n\n".format(items[0], a))
            outputFile.close()
            continue
        if fb >= -0.01 and fb <= 0.01:
            outputFile = open('result.txt', 'a')
            outputFile.write("-------------------- Equation {} --------------------\n".format(index))
            outputFile.write("Considering the interval [{}, {}]\n".format(float(items[1]), float(items[2])))
            outputFile.write("{} => {}\n\n\n".format(items[0], b))
            outputFile.close()
            continue

        temporaryX =  b

        attempts = 0
        while attempts < 10:
            attempts = attempts + 1
            result = expression(temporaryX)

            if result > -0.01 and result < 0.01:
                outputFile = open('result.txt', 'a')
                outputFile.write("-------------------- Equation {} --------------------\n".format(index))
                outputFile.write("Considering the interval [{}, {}]\n".format(float(items[1]), float(items[2])))
                outputFile.write("{} => {}\n\n\n".format(items[0], temporaryX))
                outputFile.close()
                break
            
            temporaryX = b - (fb * (b-a))/(fb-fa)

            a = b
            b = temporaryX
            
            fa = expression(a)
            fb = expression(b)


        if attempts >= 10:
            outputFile = open('result.txt', 'a')
            outputFile.write("-------------------- Equation {} --------------------\n".format(index))
            outputFile.write("Considering the interval [{}, {}]\n".format(float(items[1]), float(items[2])))
            outputFile.write("{} => Unable to find approximate root\n\n\n".format(items[0]))
            outputFile.close()

    inputFile.close()

main()
print("Done. See the results on result.txt")