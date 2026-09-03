import cv2

img = cv2.imread("images/sample.jpg")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# now we apply gausian blur
blur = cv2.GaussianBlur(gray, (5,5), 0)

# thershold both the versions
_, thresh_gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
_, thresh_blur = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Grayscale", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Threshold (no blur)", thresh_gray)
cv2.imshow("Threshold (blur)", thresh_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()