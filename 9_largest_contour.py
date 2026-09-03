import cv2

img  = cv2.imread("images/sample.jpg")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 50, 150)

contours, _ = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# to find largest contour
largest_contour = None
max_area = 0

for cnt in contours:
    area = cv2.contourArea(cnt)
    if max_area < area:
        max_area = area
        largest_contour = cnt

# Now we draw the largest contour
output = img.copy()

if largest_contour is not None:
    cv2.drawContours(output, [largest_contour], -1, (0, 255, 0), 2)

cv2.imshow("Largest contour", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
    