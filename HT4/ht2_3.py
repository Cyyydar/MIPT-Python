import sys
from HT4 import ht2_1

def readFile(path):
    with open(path, 'r') as f:
        return f.readlines()

if __name__ == '__main__':
    print(sys.argv)
    path = sys.argv[1]
    method = sys.argv[2]

    img = readFile(path)

    match method:
        case 'gamma_correction':
            ht2_1.gamma_correction(img, 1)
        case 'equalize_hist_color':
            ht2_1.equalize_hist_color(img)
        case 'RGBtoYIQ':
            ht2_1.RGBtoYIQ(img)
        case 'YIQtoRGB':
            ht2_1.YIQtoRGB(img)