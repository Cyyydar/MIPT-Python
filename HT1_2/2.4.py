
vec = [1,2,3]

mat = [
    [1,2,3],
    [3,4,5],
    [1,2,3]
]

outVec = [0] * len(vec)
for i in range(len(mat)):
    for j in range(len(vec)):
        outVec[i] += mat[i][j] * vec[j]
print(outVec)