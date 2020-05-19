import numpy as np
import cv2


def preprocessing(rawimg):
    src = cv2.imread(rawimg)
    processedSrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    return processedSrc

def pad_with(array, pad_width, iaxis, kwargs):
    pad_value = kwargs.get("padder", 0)
    array[:pad_width[0]] = pad_value
    array[-pad_width[1]:] = pad_value
    return array

def padding(array, pad_width):

    paddingarray = np.pad(array, pad_width, pad_with)
    return paddingarray

def convolution(rowlength, columnlength, kernel, array):

    temp = np.zeros((rowlength, columnlength), dtype=np.float_)
    for i in range(rowlength):
        for j in range(columnlength):
            temp[i][j] = np.inner(kernel, array[i:i+3, j:j+3].flatten())
    return temp


preImage = preprocessing("Lenna.png")
image = padding(preImage, 1)
row = preImage.shape[0]
column = preImage.shape[1]

#Roberts
roberts_x = np.array([0, 0, -1,
                      0, 1, 0,
                      0, 0, 0],dtype=object)

roberts_y = np.array([-1, 0, 0,
                      0, 1, 0,
                      0, 0, 0], dtype=object)

#Prewitt
prewitt_x = np.array([-1, -1, -1,
                      0, 0, 0,
                      1, 1, 1], dtype=object)

prewitt_y = np.array([1, 0, -1,
                      1, 0, -1,
                      1, 0, -1], dtype=object)

#Sobel
sobel_x = np.array([-1, -2, -1,
                    0, 0, 0,
                    1, 2, 1], dtype=object)

sobel_y = np.array([1, 0, -1,
                    2, 0, -2,
                    1, 0, -1], dtype=object)

roberts_x = convolution(row, column, roberts_x, image)
roberts_gx = cv2.convertScaleAbs(roberts_x)
roberts_y = convolution(row, column, roberts_y, image)
roberts_gy = cv2.convertScaleAbs(roberts_y)
roberts_g = cv2.addWeighted(roberts_gx, 1, roberts_gy, 1, 0)
cv2.imshow("robert", roberts_g)

prewitt_x = convolution(row, column, prewitt_x, image)
prewitt_gx = cv2.convertScaleAbs(prewitt_x)
prewitt_y = convolution(row, column, prewitt_y, image)
prewitt_gy = cv2.convertScaleAbs(prewitt_y)
prewitt_g = cv2.addWeighted(prewitt_gx, 1, prewitt_gy, 1, 0)
cv2.imshow("prewitt", prewitt_g)

sobel_x = convolution(row, column, sobel_x, image)
sobel_gx = cv2.convertScaleAbs(sobel_x)
sobel_y = convolution(row, column, sobel_y, image)
sobel_gy = cv2.convertScaleAbs(sobel_y)
sobel_g = cv2.addWeighted(sobel_gx, 1, sobel_gy, 1, 0)
cv2.imshow("sobel", sobel_g)

cv2.waitKey(0)
cv2.destroyAllWindows()