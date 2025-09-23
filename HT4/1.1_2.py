import time
import random

def multVectorMatrix(vec: list, mat: list) -> list:
    row = 0
    outVec = [0] * len(vec)
    for i in range(len(mat)):
        for j in range(len(vec)):
            outVec[i] += mat[i][j] * vec[j]
    return outVec

def multMatrixMatrix(mat1: list, mat2: list) -> list:
    if len(mat1[0]) != len(mat2):
        return []

    out = [[0]* len(mat1)] * len(mat2[0])

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                out[i][j] += mat1[i][k] * mat2[k][j]
    
    return out

def traceMatrix(mat: list):
    tr = 0
    for i in range(len(mat)):
        tr += mat[i][i]

def scalMult(vec1: list, vec2: list):
    if len(vec1) != len(vec2):
        return 0
    result = 0
    for i in range(len(vec1)):
        result += vec1[i] * vec2[i]

    return result

def hist(vec, bins):
    hist = [""] * bins
    step = (max(vec) - min(vec)) / bins

    print(step)
    for num in vec:
        if num!=max(vec):
            hist[int((num - min(vec)) / step)] += "■"
        else:
            hist[-1]+="■"

    for i in range(len(hist)):
        print(f"{i+1}-й бин: {hist[i]}")

def kernelFilter(vec, kernel):
    k_mid = len(kernel)//2

    result = []

    for i in range(len(vec)):
        s = 0
        for j in range(len(kernel)):
            idx = i + j - k_mid
            if 0 <= idx < len(vec):
                s += vec[idx] * kernel[j]
        result.append(s)
    return result

def readFile(path):
    with open(path, 'r') as f:
        print(f.readlines())
        return f.readlines()

def writeFile(path, data):
    with open(path, "w") as f:
        f.writelines(data)

def appendFile(path, data):
    with open(path, "a") as f:
        f.writelines(data)

def measure_time():
    sizes = [10, 100, 500]
    writeFile("time.txt", "")
    for s in sizes:
        mat = [[random.random() for _ in range(s)] for _ in range(s)]
        vec = [random.random() for _ in range(s)]
        
        start = time.time()

        multVectorMatrix(vec, mat)
        multMatrixMatrix(mat, mat)
        traceMatrix(mat)
        scalMult(vec, vec)
        hist(vec, 10)
        kernelFilter(vec, [-1, 0, 1])

        appendFile("time.txt", f"Размерность {s} - время {time.time() - start}\n")
        
measure_time()