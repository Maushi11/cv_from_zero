import cv2

# we'll read the image first
img = cv2.imread("images/sample.jpg")
print(img)
# now we'll show the image
cv2.imshow("My first image", img)

# the image will beshown till any key is pressed
cv2.waitKey(0)

# after the key is pressed all the windows are closed
cv2.destroyAllWindows()