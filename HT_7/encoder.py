import cv2
import numpy as np
from abc import ABC, abstractmethod

class HistogramStrategy(ABC):
    @abstractmethod
    def save(self, img, path):
        pass
    @abstractmethod
    def load(self, path):
        pass

class NpyHistogram(HistogramStrategy):
    def save(self, img, path):
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        np.save(path, hist)

    def load(self, path):
        return np.load(path, allow_pickle=True)

class TxtHistogram(HistogramStrategy):
    def save(self, img, path):
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        np.savetxt(path, hist)
    def load(self, path):
        return np.loadtxt(path)
