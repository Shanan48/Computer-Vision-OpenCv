from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

"""Just as in the edge detection methods discussed in the
previous chapter, we are going to convert our image to
grayscale and then apply a Gaussian blur, making it easier for the edge detector to find the outline of the coins. We
use a much larger blurring size this time, with s = 11. All
this is handled on"""

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Image", image)

"""We then obtain the edged image by applying the Canny
edge detector on Line 24. Again, just as in previous edge
detection examples, any gradient values below 30 are considered non-edges whereas any values above 150 are considered sure edges"""
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)

"""Now that we have the outlines of the coins, we can find
the contours of the outlines. We do this using the cv2.
findContours function

The first argument to cv2.findContours is our edged image. It’s important to note that this function is destructive
to the image you pass in. If you intend using that image
later on in your code, it’s best to make a copy of it using the NumPy copy method.

The second argument is the type of contours we want.
We use cv2.RETR_EXTERNAL to retrieve only the outermost
contours (i.e., the contours that follow the outline of the
coin). We can also pass in cv2.RETR_LIST to grab all contours. Other methods include hierarchical contours using
cv2.RETR_COMP and cv2.RETR_TREE, but hierarchical contours are outside the scope of this book

Our last argument is how we want to approximate the
contour. We use cv2.CHAIN_APPROX_SIMPLE to compress
horizontal, vertical, and diagonal segments into their endpoints only. This saves both computation and memory. If
we wanted all the points along the contour, without compression, we can pass in cv2.CHAIN_APPROX_NONE; however,
be very sparing when using this function. Retrieving all
points along a contour is often unnecessary and is wasteful of resources.

Our contours cnts is simply a Python list. We can use
the len function on it to count the number of contours that
were returned. We do this on Line 20 to show how many
contours we have found
"""

(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

"""This method returns
a 3-tuple of: (1) our image after applying contour detection (which is modified and essentially destroyed), (2) the
contours themselves, cnts, and (3) the hierarchy of the contours (see below)."""

print("I count {} coins in this image".format(len(cnts)))
coins = image.copy()

"""A call to cv2.drawContours draws the actual contours on
our image. The first argument to the function is the image
we want to draw on. The second is our list of contours.
Next, we have the contour index. By specifying a negative
value of −1, we are indicating that we want to draw all of
the contours. However, we would also supply an index i,
which would be the i’th contour in cnts. This would allow
us to draw only a single contour rather than all of them"""

cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

"""The fourth argument to the cv2.drawContours function
is the color of the line we are going to draw. Here, we use a green color

Finally, our last argument is the thickness of the line we
are drawing. We’ll draw the contour with a thickness of
two pixels
"""

cv2.drawContours(coins, cnts, 0, (0, 255, 0), 2)
cv2.drawContours(coins, cnts, 1, (0, 255, 0), 2)
cv2.drawContours(coins, cnts, 2, (0, 255, 0), 2)