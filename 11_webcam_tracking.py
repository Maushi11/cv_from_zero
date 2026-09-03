import cv2
from collections import deque

cap = cv2.VideoCapture(0)

trail = deque(maxlen=50)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
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

    if largest_contour is not None:
        M = cv2.moments(largest_contour)
        if M["m00"] != 0 :
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            trail.appendleft((cx,cy))

            sum_x = 0
            sum_y = 0

            for point in trail:
                sum_x += point[0]
                sum_y += point[1]

            smooth_x = int(sum_x / len(trail))
            smooth_y = int(sum_y / len(trail))

            cv2.circle(frame, (smooth_x,smooth_y), 5, (0, 0, 255), -1)

    for i in range(1, len(trail)):
        cv2.line(frame, trail[i-1], trail[i], (255, 0, 0), max(1, 5 - i))

    cv2.imshow("Tracking", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
