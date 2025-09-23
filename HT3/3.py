def channel_filter(filter2d):
    def wrapper(img):        
        M = len(img)
        N = len(img[0]) 
        chanels = 3
        out = [[[0.0 * chanels] * M] * N]
        
        for ch in range(chanels):
            chanel = [[0.0] * M] * N
            for i in range(M):
                for j in range(N):
                    chanel[i][j] = img[i][j][ch]

            filtred_chanel = filter2d(chanel)

            for i in range(M):
                for j in range(N):
                    out[i][j][ch] = filtred_chanel[i][j]
        return out
    
    return wrapper