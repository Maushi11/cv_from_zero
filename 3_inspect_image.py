import cv2

img = cv2.imread("images/sample.jpg")

if img is None:
    print("Image is not found !")
    exit()

print("Type of image", type(img))
print("Shape of image", img.shape)

print("\nFirst pixle value", img[0][0])