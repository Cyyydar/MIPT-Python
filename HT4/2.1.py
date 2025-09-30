def clamp_int(x: int, lo: int = 0, hi: int = 255):
    if x < lo: return lo
    if x > hi: return hi
    return x

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

def equalize_hist_channel(img):
    H = len(img)
    W = len(img[0])

    hist = [0] * 256
    total = 0
    for row in img:
        for v in row:
            iv = int(v)
            if iv < 0: iv = 0
            elif iv > 255: iv = 255
            hist[iv] += 1
            total += 1

    cdf = [0] * 256
    running = 0
    for i in range(256):
        running += hist[i]
        cdf[i] = running

    if total == 0:
        return [row[:] for row in img]

    cdf_min = next((val for val in cdf if val > 0), 0)

    lut = [0] * 256
    denom = total - cdf_min
    if denom <= 0:
        lut = [0] * 256
    else:
        for i in range(256):
            val = (cdf[i] - cdf_min) / denom
            if val < 0: val = 0.0
            elif val > 1: val = 1.0
            lut[i] = int(round(val * 255))

    out = [[0] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            v = int(img[y][x])
            if v < 0: v = 0
            elif v > 255: v = 255
            out[y][x] = lut[v]

    return out

def equalize_hist_color(img_rgb):
    if not img_rgb or not img_rgb[0]:
        return []

    H = len(img_rgb)
    W = len(img_rgb[0])

    Y = [[0]*W for _ in range(H)]
    U = [[0]*W for _ in range(H)]
    V = [[0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            yiq = RGBtoYIQ(img_rgb[y][x])
            Y[y][x] = clamp_int(yiq[0])
            U[y][x] = yiq[1] 
            V[y][x] = yiq[2]

    Y_eq = equalize_hist_channel(Y)

    out = [[(0,0,0)]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            rgb = YIQtoRGB([Y_eq[y][x], U[y][x], V[y][x]])
            out[y][x] = rgb

    return out


def gamma_correction(img, gamma):
    lut = [0] * 256
    
    for i in range(256):
        val = ((i / 256.0) ** gamma) * 255.0
        lut[i] = clamp_int(int(round(val)))


    H = len(img)
    W = len(img[0])
    out = [[(0,0,0)]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            r,g,b = img[y][x]
            r = int(r); g = int(g); b = int(b)
            r = 0 if r < 0 else (255 if r > 255 else r)
            g = 0 if g < 0 else (255 if g > 255 else g)
            b = 0 if b < 0 else (255 if b > 255 else b)
            out[y][x] = (lut[r], lut[g], lut[b])
    return out