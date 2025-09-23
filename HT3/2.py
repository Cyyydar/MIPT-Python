import random

def createVector(N) -> list:
    vec = []
    for _ in range(N):
        vec.append(random.random() % 1)
    return vec

def createMatrix(N: int, M: int) -> list:
    mat = []
    for _ in range(N):
        row = createVector(M)
        mat.append(row)
    return mat

def printVector(vec: list):
    print(vec)

def printMatrix(mat: list):
    for i in mat:
        printVector(i)

def multVectorMatrix(vec: list, mat: list) -> list:
    row = 0
    outVec = [0] * len(vec)
    for i in range(len(mat)):
        for j in range(len(vec)):
            outVec[i] += mat[i][j] * vec[j]
    return outVec
        
def diagSum(mat: list):
    if len(mat) != len(mat[0]):
        print("Матрица не квадратная")
        return
    sum = 0
    for i in range(len(mat)):
        sum += mat[i][i]

    return sum

mat = createMatrix(3, 3)
printMatrix(mat)
print(diagSum(mat))