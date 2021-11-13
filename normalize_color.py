import cv2
import numpy as np
import matplotlib.pyplot as plt

# Прочитать оригинальное изображение
img = cv2.imread('2.png')

# Получить высоту и ширину изображения
height = img.shape[0]
width = img.shape[1]

# Создать изображение
grayimg = np.zeros((height, width, 3), np.uint8)

# Максимальная обработка изображения в градациях серого
for i in range(height):
    for j in range(width):
        # Получить изображение R G B максимум
        gray = max(img[i, j][0], img[i, j][1], img[i, j][2])
        # Назначение пикселей в градациях серого серого цвета = максимум (R, G, B)
        grayimg[i, j] = np.uint8(gray)

# Показать изображение
cv2.imshow("src", img)
cv2.imshow("gray", grayimg)

# Ждать показа
cv2.waitKey(0)
cv2.destroyAllWindows()
