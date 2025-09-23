def multVectorMatrix(vec: list, mat: list) -> list:
    row = 0
    outVec = [0] * len(vec)
    for i in range(len(mat)):
        for j in range(len(vec)):
            outVec[i] += mat[i][j] * vec[j]
    return outVec

def RGBtoYIQ(RGB: list) -> list:
    mat = [[0.299,  0.587,  0.114],
           [0.5959,-0.2746,-0.3213],
           [0.2115,-0.5227, 0.3112]]
    print(multVectorMatrix(RGB, mat))
    return multVectorMatrix(RGB, mat)


def YIQtoRGB(YIQ: list) -> list:
    mat = [[1, 0.956, 0.619],
           [1,-0.272,-0.647],
           [1,-1.106, 1.703]]
    return multVectorMatrix(YIQ, mat)


def auto_convert(vec: list) -> list:
    
    if vec[3] == 0:
        result = RGBtoYIQ(vec[0:3])
        result.append(1)
    else:
        result = YIQtoRGB(vec[0:3])
        result.append(0)
    return result


RGB = [116,234,100, 0]
YIQ = auto_convert(RGB)
print(f"RGB {RGB} to YIQ = {auto_convert(RGB)}")
print(f"YIQ {YIQ} to RGB = {auto_convert(YIQ)}")