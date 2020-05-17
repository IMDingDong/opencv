import cv2

src = cv2.imread("Lenna.png", cv2.IMREAD_GRAYSCALE)
dst = cv2.equalizeHist(src)

cv2.imshow("source", src)
cv2.imshow("destination", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
