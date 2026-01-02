import cv2

img = cv2.imread("images/sample.jpg")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("original shape", img.shape)
print("grayscale shape", gray.shape)

cv2.imshow("Color Image", img)
cv2.imshow("Grayscale image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()