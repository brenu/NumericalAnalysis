import parser
import random
import re

userInput = input("Insert the function: ")
a = float(input("Insert the interval's element A (positive): "))
b = float(input("Insert the interval's element B (negative): "))

while not re.match("^[A-Za-z0-9 \+\-\*\(\)\%\/]*$", userInput):
    print("[*] Only mathematical expressions are accepted.")
    userInput = input("Insert the function: ")
    a = float(input("Insert the interval's element A (positive): "))
    b = float(input("Insert the interval's element B (negative): "))
else:
    evaluatedExpression = parser.expr(userInput).compile()

    expressionZero = 0
    temporaryX = 1
    attempts = 0

    print("\n")

    while eval(evaluatedExpression, {'x': temporaryX, 'X': temporaryX}) > 0.01 or eval(evaluatedExpression, {'x': temporaryX, 'X': temporaryX}) < 0.01:
        attempts = attempts + 1
        if attempts <= 10000:
            temporaryX = (a + b) / 2
            result = eval(evaluatedExpression, {'x': temporaryX, 'X': temporaryX})

            print("Testing x={} => result: {}".format(temporaryX, result))

            if result < -0.01:
                b = temporaryX
            elif result > 0.01:
                a = temporaryX
            else:
                expressionZero = temporaryX
                print("\n\nThe function's zero, considering a deviation of 10⁻², is: ", expressionZero)
                break
        else:
            print("\n\nSorry, we couldn't find any root for this expression :(")
            break
    
    