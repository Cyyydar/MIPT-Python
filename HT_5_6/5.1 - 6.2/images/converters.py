from images.images import BinaryImage
from images.images import ColorImage
from images.images import MonochromeImage


class ImageConverter:

    @staticmethod
    def binary_to_binary(img: BinaryImage):
        return img

    @staticmethod
    def monochrome_to_monochrome(img: MonochromeImage):
        all_pixels = [px for row in img.data for px in row]
        min_px, max_px = min(all_pixels), max(all_pixels)
        if max_px == min_px:
            return MonochromeImage(img.data)
        scale = 255 / (max_px - min_px)
        new_data = [[int((px - min_px) * scale) for px in row] for row in img.data]
        return MonochromeImage(new_data)

    @staticmethod
    def color_to_color(img: ColorImage):
        channels = list(zip(*[pixel for row in img.data for pixel in row]))
        mins = [min(ch) for ch in channels]
        maxs = [max(ch) for ch in channels]

        new_data = []
        for row in img.data:
            new_row = []
            for (r, g, b) in row:
                new_r = int(255 * (r - mins[0]) / (maxs[0] - mins[0] + 1e-6))
                new_g = int(255 * (g - mins[1]) / (maxs[1] - mins[1] + 1e-6))
                new_b = int(255 * (b - mins[2]) / (maxs[2] - mins[2] + 1e-6))
                new_row.append([new_r, new_g, new_b])
            new_data.append(new_row)
        return ColorImage(new_data)

    @staticmethod
    def color_to_monochrome(img: ColorImage):
        return MonochromeImage(img.data)

    @staticmethod
    def monochrome_to_color(img: MonochromeImage, palette=None):
        new_data = []
        for row in img.data:
            new_row = []
            for px in row:
                if palette and px in palette:
                    new_row.append(list(palette[px]))
                else:
                    new_row.append([px, px, px])
            new_data.append(new_row)
        return ColorImage(new_data)

    @staticmethod
    def monochrome_to_binary(img: MonochromeImage, threshold=128):
        data = [[255 if px > threshold else 0 for px in row] for row in img.data]
        return BinaryImage(data)

    @staticmethod
    def binary_to_monochrome(img: BinaryImage):
        h, w = len(img.data), len(img.data[0])
        result = [[0 for _ in range(w)] for _ in range(h)]
        white_coords = [(y, x) for y in range(h) for x in range(w) if img.data[y][x] == 255]

        for y in range(h):
            for x in range(w):
                if img.data[y][x] == 255:
                    result[y][x] = 0
                else:
                    dist = min((abs(y - wy) + abs(x - wx)) for wy, wx in white_coords) if white_coords else 0
                    result[y][x] = min(int(dist * 20), 255) 
        return MonochromeImage(result)

    @staticmethod
    def color_to_binary(img: ColorImage, threshold=128):
        mono = ImageConverter.color_to_monochrome(img)
        return ImageConverter.monochrome_to_binary(mono, threshold)

    @staticmethod
    def binary_to_color(img: BinaryImage, palette=None):
        mono = ImageConverter.binary_to_monochrome(img)
        return ImageConverter.monochrome_to_color(mono, palette)