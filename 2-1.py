import cv2

src = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
alpha=50

dst1 = src+alpha
dst2 = src-alpha
dst3 = src*alpha
dst4 = src/alpha
dst5 = cv2.bitwise_and(src, alpha)
dst6 = cv2.bitwise_xor(src, alpha)

cv2.imshow("source", src)
cv2.imshow("+", dst1)
cv2.imshow("-", dst2)
cv2.imshow("*", dst3)
cv2.imshow("/", dst4)
cv2.imshow("AND", dst5)
cv2.imshow("XOR", dst6)

cv2.waitKey(0)
cv2.destroyAllWindows()
