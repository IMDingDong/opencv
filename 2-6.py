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

#MASK1
mask1_x = np.array([0, -1, 0,
                    -1, 4, -1,
                    0, -1, 0], dtype=object)

mask1_y = np.array([0, -1, 0,
                    -1, 4, -1,
                    0, -1, 0], dtype=object)

#MASK2
mask2_x = np.array([1, -2, 1,
                    -2, 4, -2,
                    1, -2, 1], dtype=object)

mask2_y = np.array([1, -2, 1,
                    -2, 4, -2,
                    1, -2, 1], dtype=object)

#MASK3
mask3_x = np.array([-1, -1, -1,
                    -1, 8, -1,
                    -1, -1, -1], dtype=object)

mask3_y = np.array([-1, -1, -1,
                    -1, 8, -1,
                    -1, -1, -1], dtype=object)


mask1_x = convolution(row, column, mask1_x, image)
mask1_gx = cv2.convertScaleAbs(mask1_x)
mask1_y = convolution(row, column, mask1_y, image)
mask1_gy = cv2.convertScaleAbs(mask1_y)
mask1_g = cv2.addWeighted(mask1_gx, 1, mask1_gy, 1, 0)
cv2.imshow("mask1", mask1_g)

mask2_x = convolution(row, column, mask2_x, image)
mask2_gx = cv2.convertScaleAbs(mask2_x)
mask2_y = convolution(row, column, mask2_y, image)
mask2_gy = cv2.convertScaleAbs(mask2_y)
mask2_g = cv2.addWeighted(mask2_gx, 1, mask2_gy, 1, 0)
cv2.imshow("mask2", mask2_g)

mask3_x = convolution(row, column, mask3_x, image)
mask3_gx = cv2.convertScaleAbs(mask3_x)
mask3_y = convolution(row, column, mask3_y, image)
mask3_gy = cv2.convertScaleAbs(mask3_y)
mask3_g = cv2.addWeighted(mask3_gx, 1, mask3_gy, 1, 0)
cv2.imshow("mask3", mask3_g)

cv2.waitKey(0)
cv2.destroyAllWindows()