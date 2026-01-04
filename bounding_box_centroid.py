import cv2

img = cv2.imread("images/sample.jpg")

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

largest_contour = None
max_area = 0

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > max_area:
        max_area = area
        largest_contour = cnt

output = img.copy()
if largest_contour is not None:
    cv2.drawContours(output, [largest_contour], -1, (0, 255, 0), 0)

# bounding box
x, y, w, h = cv2.boundingRect(largest_contour)

cv2.rectangle(
    output,
    (x,y),
    (x + w, y + h),
    (255, 0, 0),
    2
)

# Centroid
M = cv2.moments(largest_contour)
if M["m00"] != 0:
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])

    cv2.circle(output, (cx, cy), 5, (0, 0, 255), -1)

cv2.imshow("Largest contour", output)
cv2.waitKey(0)
cv2.destroyAllWindows()