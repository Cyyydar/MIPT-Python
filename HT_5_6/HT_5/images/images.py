class Image:
    def __init__(self, data):
        # data — это двумерный (список списков) или трёхмерный список (для RGB)
        self.data = data

class BinaryImage(Image):
    def __init__(self, data):
        # Принудительно приводим все значения к 0 или 255
        processed = [[255 if px > 127 else 0 for px in row] for row in data]
        super().__init__(processed)


class MonochromeImage(Image):
    def __init__(self, data):
        # Если данные RGB, усредняем
        if isinstance(data[0][0], list):
            processed = []
            for row in data:
                new_row = []
                for (r, g, b) in row:
                    gray = (r + g + b) // 3
                    new_row.append(gray)
                processed.append(new_row)
        else:
            processed = data
        super().__init__(processed)


class ColorImage(Image):
    def __init__(self, data):
        # Проверка: каждый пиксель должен быть списком из 3 элементов
        if not isinstance(data[0][0], list) or len(data[0][0]) != 3:
            raise ValueError("Цветное изображение должно состоять из троек (R,G,B)")
        super().__init__(data)
