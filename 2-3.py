import cv2
import numpy as np
image = cv2.imread("Lenna.png")

rows, cols = image.shape[:2]

filter_3x3 = np.ones((3, 3), np.float32) / 9.0
filter_5x5 = np.ones((5, 5), np.float32) / 25.0
filter_7x7 = np.ones((7, 7), np.float32) / 49.0

cv2.imshow('Source', image)

dst = cv2.filter2D(image, -1, filter_3x3)
cv2.imshow('filter_3x3', dst)

dst = cv2.filter2D(image, -1, filter_5x5)
cv2.imshow('filter_5x5', dst)

dst = cv2.filter2D(image, -1, filter_7x7)
cv2.imshow('filter_7x7', dst)

cv2.waitKey()