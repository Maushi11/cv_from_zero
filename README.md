## Learning Computer Vision from Basics

I am gonna write here anything i learnt or found 

## Phase 1 - start
- how to import cv
- how to use the cv commands 
- how does the computer reads the image

## Phase 2 - learning BGR
- image is a NumPy array 
- image shape - it shows the width height and the number of values a single pixel will have
- we have three different values for the image ie. BGR - (Blue, Green, Red)
- this values give the intensity of the pixel towards each of the three color

## Phase 3 - Grayscale
- its shape doesnt show the third parameter since everything is gray ie. its either black(0) or white(255) Everything in between = shades of gray
- it stores intensity of the pixels brightness and not the color this time
- [B, G, R] → [intensity]

## Phase 4 - Threshold
- convert the grayascale into a completely black and white image ie. grayscale → binary image
- set the threshold value like 127 (its the intensity) so if above it then white or below means black
- it might fail if the image is to light or shadowy etc.
- ret, thresh
- cv2.threshold() actually returns TWO values 
- ret → the threshold value used
- thresh → the output image
- But we already KNOW the threshold value, so we don’t care.

## Phase 5 - Blur
- blur it doesnt look good to human eyes like its thershold version but it is good for the computer 
- for algorithm it hates the sharp edges fine details and texture 
- Too sharp → noisy
- Too blurry → lost structure
- blur = cv2.GaussianBlur(gray, (5, 5), 0)
- in this (5,5) is the Kernel size - “How big of an area should OpenCV look at to blur a pixel?”
- Bigger kernel → more blur
- Smaller kernel → less blur
- and 0 is the blur strength so if we set it 0 then CV atomaticaly decides the strength based on the kernel size

## Phase 6 - Edges
- Edge detection only works when there is contrast
- If foreground and background have similar brightness → no edge.
- edges = cv2.Canny(blur, 50, 150) in this 50 is the low threshold and 150 is the high threshold
- Strong edges (>150) → always kept
- Weak edges (50–150) → kept only if connected to strong edges
- Noise (<50) → discarded
- This is called hysteresis thresholding.
- Color → Grayscale → Blur → Edges
- Color → too much info
- Grayscale → structure
- Blur → stability
- Edges → shape

## Phase 7 - Contours
- contours, hierarchy = cv2.findContours(
    binary_image,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
- cv2.RETR_EXTERNAL - This tells OpenCV: “Only give me outermost contours”
- cv2.CHAIN_APPROX_SIMPLE - This controls how many points are stored Straight lines compressed Only corner points kept
- cv2.drawContours(
    frame,
    contours,
    -1,
    (0,255,0),
    2
)
    Breakdown:
    Parameters
    frame → image to draw on
    contours → list of contours
    -1 → draw all contours
    (0,255,0) → green color
    2 → thickness
- so contour works on the principle of finding a closed object 