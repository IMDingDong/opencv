import cv2
import numpy as np

colorSrc = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
src = cv2.cvtColor(colorSrc, cv2.COLOR_BGR2GRAY)

dst1 = cv2.resize(src, dsize=(512, 512), interpolation=cv2.INTER_AREA)
dst1 = cv2.resize(dst1, dsize=(235, 313), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize=(256, 256), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(dst2, dsize=(235, 313), interpolation=cv2.INTER_AREA)
dst3 = cv2.resize(src, dsize=(128, 128), interpolation=cv2.INTER_AREA)
dst3 = cv2.resize(dst3, dsize=(235, 313), interpolation=cv2.INTER_AREA)
dst4 = cv2.resize(src, dsize=(64, 64), interpolation=cv2.INTER_AREA)
dst4 = cv2.resize(dst4, dsize=(235, 313), interpolation=cv2.INTER_AREA)
dst5 = cv2.resize(src, dsize=(32, 32), interpolation=cv2.INTER_AREA)
dst5 = cv2.resize(dst5, dsize=(235, 313), interpolation=cv2.INTER_AREA)
dst6 = cv2.resize(src, dsize=(16, 16), interpolation=cv2.INTER_AREA)
dst6 = cv2.resize(dst6, dsize=(235, 313), interpolation=cv2.INTER_AREA)

dst7 = src - 255
dst8 = src - 15
dst9 = src - 3
dst10 = src - 1

cv2.imshow("src", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.imshow("dst4", dst4)
cv2.imshow("dst5", dst5)
cv2.imshow("dst6", dst6)

cv2.imshow("dst7", dst7)
cv2.imshow("dst8", dst8)
cv2.imshow("dst9", dst9)
cv2.imshow("dst10", dst10)

cv2.waitKey(0)
cv2.destroyAllWindows()