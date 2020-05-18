import cv2
import numpy as np
image = cv2.imread("Lenna.png")

kernel_sharpen_1 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
kernel_sharpen_2 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
kernel_sharpen_3 = np.array([[1,-2,1],[-2,5,-2],[1,-2,1]])

output_1 = cv2.filter2D(image,-1,kernel_sharpen_1)
output_2 = cv2.filter2D(image,-1,kernel_sharpen_2)
output_3 = cv2.filter2D(image,-1,kernel_sharpen_3)

cv2.imshow('sharpening1',output_1)
cv2.imshow('sharpening2',output_2)
cv2.imshow('sharpening3',output_3)
cv2.waitKey()