import cv2 as cv
import numpy as np

# Load the image
img_bgr = cv.imread('3_small.jpg')

# Convert the image to grayscale
img_gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)

# Load the template
template = cv.imread('template.jpg', 0)

# Get the width and height of the template
template_w, template_h = template.shape[::-1]

# Find the results in the loaded image
result = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

# define a threshold
threshold = 0.8

# Find the locations of the results that are greater than or eaqual to the threshold
location = np.where(result >= threshold)

# Mark all matches on the picture. For all the points of all the locations
for point in zip(*location[::-1]):
    # Draw a rectangle taking the shape of the template and placing it over the match
    cv.rectangle(img_bgr, point, (point[0] + template_w, point[1] + template_h), (0, 255, 255), 2)

cv.imshow('Detected', img_bgr)
cv.waitKey(10000)
cv.destroyAllWindows()
