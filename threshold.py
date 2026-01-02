import cv2

img = cv2.imread("images/sample.jpg")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Now we apply threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

print("Grayscale shape:", gray.shape)
print("Threshold shape:", thresh.shape)

cv2.imshow("Grayscale", gray)
cv2.imshow("Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()