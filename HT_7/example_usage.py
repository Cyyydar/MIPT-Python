from image import ImageFactory
from hist import save_histogram, load_histogram
from encoder import NpyHistogram
import cv2
import os

# Пути к изображениям
mono_path = "images/cat_gray.jpg"   # замените на свой путь
color_path = "images/cat.jpg" # замените на свой путь

# ===============================
# Обработка монохромного изображения
# ===============================

print("=== Обработка монохромного изображения ===")
mono = ImageFactory.create_processor(mono_path, "mono")

# preprocess (Gaussian)
mono.preprocess()
cv2.imwrite("results/mono_gaussian.jpg", mono.gray)

# extract_features (Canny + Hu)
mono.extract_features()
cv2.imwrite("results/mono_canny.jpg", mono.img)

print("Hu моменты (монохром):", mono.hu_moments)


# ===============================
# Обработка цветного изображения
# ===============================

print("=== Обработка цветного изображения ===")
color = ImageFactory.create_processor(color_path, "color")

# preprocess (Gray + Threshold + Distance Transform)
color.preprocess()

# Сохраняем промежуточные этапы

cv2.imwrite("results/color_gray.jpg", color.gray)

cv2.imwrite("results/color_thresh.jpg", color.thresh)

# extract_features (Watershed + Hu)
color.extract_features()
cv2.imwrite("results/color_watershed.jpg", color.img)

print("Hu моменты (цветное):", color.hu_moments)


# ===============================
# Работа с гистограммой
# ===============================

hist_strategy = NpyHistogram()
hist_file = "results/mono_hist.npy"

# Сохранение
save_histogram(hist_strategy, mono.img, hist_file)
print(f"Гистограмма сохранена: {hist_file}")

# Загрузка
if os.path.exists(hist_file):
    loaded_hist = load_histogram(hist_strategy, hist_file)
    print("Гистограмма загружена:",
          loaded_hist.flatten())
else:
    print("Ошибка: файл гистограммы не найден!")