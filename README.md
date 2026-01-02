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