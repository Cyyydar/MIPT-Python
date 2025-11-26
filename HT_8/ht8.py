import numpy as np
from functools import partial

def linear_iter(img):
    h, w = img.shape[:2]
    for y in range(h):
        for x in range(w):
            yield y, x

def spiral_iter(img):
    h, w = img.shape[:2]
    cy, cx = h // 2, w // 2

    yield cy, cx

    step = 1
    while step < max(h, w):
        for _ in range(step):
            cx += 1
            if 0 <= cx < w and 0 <= cy < h:
                yield cy, cx
        for _ in range(step):
            cy += 1
            if 0 <= cx < w and 0 <= cy < h:
                yield cy, cx

        step += 1

        for _ in range(step):
            cx -= 1
            if 0 <= cx < w and 0 <= cy < h:
                yield cy, cx
        for _ in range(step):
            cy -= 1
            if 0 <= cx < w and 0 <= cy < h:
                yield cy, cx

        step += 1

def zigzag_iter(img):
    h, w = img.shape[:2]
    for s in range(h + w - 1):
        if s % 2 == 0:
            for y in range(min(s, h - 1), -1, -1):
                x = s - y
                if 0 <= x < w and 0 <= y < h:
                    yield y, x
        else:
            for x in range(min(s, w - 1), -1, -1):
                y = s - x
                if 0 <= x < w and 0 <= y < h:
                    yield y, x

def peano_iter(img):
    h, w = img.shape

    def peano(y0, x0, h, w, direction):
        if h == 1 and w == 1:
            yield y0, x0
            return

        if h >= w: 
            block = h // 3
            parts = [
                (y0, x0, block, w),
                (y0 + block, x0, block, w),
                (y0 + 2 * block, x0, h - 2 * block, w),
            ]

            if direction == 1:
                order = [0, 1, 2]
                next_dir = [1, -1, 1]
            else:
                order = [2, 1, 0]
                next_dir = [-1, 1, -1]

            for idx in order:
                y, x, hh, ww = parts[idx]
                yield from peano(y, x, hh, ww, next_dir[idx])
        else: 
            block = w // 3
            parts = [
                (y0, x0, h, block),
                (y0, x0 + block, h, block),
                (y0, x0 + 2 * block, h, w - 2 * block),
            ]

            if direction == 1:
                order = [0, 1, 2]
                next_dir = [1, -1, 1]
            else:
                order = [2, 1, 0]
                next_dir = [-1, 1, -1]

            for idx in order:
                y, x, hh, ww = parts[idx]
                yield from peano(y, x, hh, ww, next_dir[idx])

    yield from peano(0, 0, h, w, 1)

to_gray = lambda img: np.dot(img[..., :3], [0.299, 0.587, 0.114]).astype(np.float32)


def lazy_convolution(img, kernel):
    kh, kw = kernel.shape
    pad_h, pad_w = kh // 2, kw // 2
    h, w = img.shape

    def calc_pixel(y, x):
        acc = 0
        for i in range(kh):
            for j in range(kw):
                acc += img[y + i - pad_h, x + j - pad_w] * kernel[i, j]
        return acc

    for y in range(pad_h, h - pad_h):
        for x in range(pad_w, w - pad_w):
            yield (y, x, calc_pixel(y, x))


def apply_filter(img, kernel):
    out = np.zeros_like(img)
    for y, x, val in lazy_convolution(img, kernel):
        out[y, x] = val
    return out

def mse(a, b):
    return np.mean((a - b) ** 2)

if __name__ == "__main__":
    img = np.random.randint(0, 255, (27, 27, 3), dtype=np.uint8)

    g = to_gray(img)

    kernel = np.ones((3, 3), dtype=float) / 9.0
    filter_apply = partial(apply_filter, kernel=kernel)

    out_linear = filter_apply(g)
    out_spiral = filter_apply(g)
    out_zigzag = filter_apply(g)
    out_peano = filter_apply(g)

    print("MSE(linear/spiral) =", mse(out_linear, out_spiral))
    print("MSE(linear/zigzag) =", mse(out_linear, out_zigzag))
    print("MSE(linear/peano) =", mse(out_linear, out_peano))
    print("Если все ~ 0, то результат не зависит от порядка обхода")