import numpy as np
import matplotlib.pyplot as plt
import copy

inputFile = open("input.txt", "r")
outputFile = open("result.txt", "w")
outputFile.close()

def decomposeLU(matrix, extension):
    matrixLength = len(matrix)
    originalMatrix = copy.deepcopy(matrix)
    originalExtension = copy.deepcopy(extension)

    identityMatrix = np.eye(matrixLength, matrixLength).tolist()

    for j in range(matrixLength-1):
        for i in range(j+1, matrixLength):
            identityMatrix[i][j] = matrix[i][j] / matrix[j][j]
            for k in range(j+1,matrixLength):
                matrix[i][k] = matrix[i][k] - identityMatrix[i][j]*matrix[j][k]
            matrix[i][j] = 0

    yResults = [None] * matrixLength
    yResults[0] = extension[0]/identityMatrix[0][0]
    for i in range(1, matrixLength):
        resultSum = 0
        for j in range(i-1,-1,-1):
            resultSum = resultSum +  identityMatrix[i][j] * yResults[j]
        yResults[i] = ( extension[i] - resultSum ) / identityMatrix[i][i]

    results = [None] * matrixLength
    results[matrixLength-1] = yResults[matrixLength-1]/matrix[matrixLength-1][matrixLength-1]
    for i in range(matrixLength-2,-1, -1):
        resultSum = 0
        for j in range(i+1, matrixLength):
            resultSum = resultSum +  matrix[i][j] * results[j]
        results[i] = ( yResults[i] - resultSum ) / matrix[i][i]

    printResult(originalMatrix, originalExtension, results)
            

def printResult(matrix, extension, results):
    outputFile = open("result.txt", "a")
    outputFile.write("-----------------------------------------------\n")
    outputFile.write("Found variables: ")
    for result in results:
        outputFile.write("   {}   ".format(result))

    outputFile.write("\n\n")
    outputFile.close()
    
    nx = ny = len(matrix)
    nx = nx + 1

    cellColours = [[None] * nx] * ny

    data = np.column_stack([matrix, extension])

    for i in range(nx):
        for j in range(ny):
            if i != nx-1:
                cellColours[j][i] = "#4bb543"
            else:
                cellColours[j][i] = "#4bb"

    plt.figure()
    tb = plt.table(cellText=data, loc=(0,0), cellLoc='center', cellColours=cellColours)
    

    tc = tb.properties()['children']
    for cell in tc: 
        cell.set_height(1/ny)
        cell.set_width(1/nx)

    ax = plt.gca()
    ax.set_xticks([])
    ax.set_yticks([])

    plt.title(label="Found variables: "+(len(results)*'   {:.2f}   ').format(*results),
          loc="left",
          fontstyle='italic',
          wrap=True)

    plt.show()


def calculateSpacing(array, index):
    bigger = len(str(array[0][0]))

    for item in array:
        itemLength = len(str(item[index]))
        if itemLength > bigger:
            bigger = itemLength

    return bigger


def main():
    for line in inputFile:
        line = line.split(",")
        numberOfLines = int(line[0])
        matrix = []
        matrixExtension = []

        if len(line) != numberOfLines+2:
            print("Wrong input format. Please, check it again!\n")
            return
        
        for i in range(numberOfLines):
            matrix.append(list(map(int, line[i+1].split(" "))))

        matrixExtension = list(map(int, line[-1].split(" ")))
        
        decomposeLU(matrix, matrixExtension)

    inputFile.close()

main()
print("Done. See the results on result.txt\n")