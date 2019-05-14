import cv2 as cv
import numpy as np

# Load the image
img_bgr = cv.imread('3.jpg')

img_test = cv.resize(img_bgr, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)


# Convert the image to grayscale
img_gray = cv.cvtColor(img_test, cv.COLOR_BGR2GRAY)

# Load the template
template = cv.imread('template.jpg', 0)
template_test = cv.resize(template, None, fx=2, fy=2,
                          interpolation=cv.INTER_CUBIC)

# Get the width and height of the template
template_w, template_h = template_test.shape[::-1]

# Find the results in the loaded image
result = cv.matchTemplate(img_gray, template_test, cv.TM_CCOEFF_NORMED)

# define a threshold
threshold = 0.8

# Find the locations of the results that are greater than or eaqual to the threshold
location = np.where(result >= threshold)

# Mark all matches on the picture. For all the points of all the locations
for point in zip(*location[::-1]):
    # Draw a rectangle taking the shape of the template and placing it over the match
    cv.rectangle(
        img_test, point, (point[0] + template_w, point[1] + template_h), (0, 255, 255), 2)

cv.imshow('Detected', img_test)
cv.waitKey(10000)
cv.destroyAllWindows()
