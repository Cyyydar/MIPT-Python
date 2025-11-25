import cv2
import numpy as np
from abc import ABC, abstractmethod

# ======== Шаблонный метод ========
class ImageProcessor(ABC):
    def __init__(self, img_path):
        self.img = cv2.imread(img_path)
    
    def process(self):
        self.preprocess()
        self.extract_features()
        self.show_result()
    
    @abstractmethod
    def preprocess(self):
        pass
    
    @abstractmethod
    def extract_features(self):
        pass
    
    def show_result(self):
        cv2.imshow("Result", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

class MonoProcessor(ImageProcessor):
    def preprocess(self):
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.apply_gaussian()

    def apply_gaussian(self):
        self.gray = cv2.GaussianBlur(self.gray, (5, 5), 0)

    def extract_features(self):
        self.apply_canny()
        self.img = self.edges

    def apply_canny(self):
        self.edges = cv2.Canny(self.gray, 50, 150)

# Цветное изображение
class ColorProcessor(ImageProcessor):
    def preprocess(self):
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.to_binary()
        self.distance_transform()

    def to_binary(self):
        _, self.thresh = cv2.threshold(self.gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    def distance_transform(self):
        dist = cv2.distanceTransform(self.thresh, cv2.DIST_L2, 5)
        _, sure_fg = cv2.threshold(dist, 0.7 * dist.max(), 255, 0)
        self.sure_fg = np.uint8(sure_fg)
        self.unknown = cv2.subtract(self.thresh, self.sure_fg)

    def extract_features(self):
        self.apply_watershed()

    def apply_watershed(self):
        # создаём копию исходного изображения для результатов
        img_color = self.img.copy()
        # создаём маркеры
        _, markers = cv2.connectedComponents(self.sure_fg)
        markers = markers + 1
        markers[self.unknown == 255] = 0
        markers = cv2.watershed(img_color, markers)
        # окрашиваем границы в красный
        img_color[markers == -1] = [0, 0, 255]
        self.img = img_color  # сохраняем обратно

# ======== Декоратор ========
def add_hu_moments(processor_class):
    class Decorated(processor_class):
        def extract_features(self):
            super().extract_features()
            moments = cv2.moments(getattr(self, 'gray', self.img))
            self.hu_moments = cv2.HuMoments(moments).flatten()
            print("Hu Moments:", self.hu_moments)
    return Decorated
