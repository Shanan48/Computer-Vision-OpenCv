import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

"""The first thing we do is import our packages and parse
our arguments. We then load our image, convert it to grayscale, and blur it using the Gaussian blurring method. By applying a blur prior to edge detection, we will help remove
“noisy” edges in the image that are not of interest to us.
Our goal here is to find only the outlines of the coins.
Applying the Canny edge detector is performed on Line
23 using the cv2.Canny function. The first argument we
supply is our blurred, grayscale image. Then, we need to
provide two values: threshold1 and threshold2."""

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)

canny = cv2.Canny(image, 30, 150)

"""Any gradient value larger than threshold2 is considered
to be an edge. Any value below threshold1 is considered not to be an edge. Values in between threshold1
and threshold2 are either classified as edges or non-edges
based on how their intensities are “connected”. In this case,
any gradient values below 30 are considered non-edges whereas any values above 150 are considered edges"""

cv2.imshow("Canny", canny)
cv2.waitKey(0)

"""Notice how the edges are more “crisp”. We have substantially less noise than when we used the Laplacian or Sobel
gradient images. Furthermore, the outline of our coins are
clearly revealed.
In the next chapter, we’ll continue to make use of the
Canny edge detector and use it to count the number of
coins in our image"""

"""Further Reading

Just like thresholding is a common method for segmenting foreground objects from background objects,
the same can be said for edge detection – only instead
of obtaining a large blob representing the foreground,
the Canny detector gives us the outline.
However, a common challenge of using the Canny edge
detector is getting the lower and upper edge thresholds just right. In order to help you (automatically)
determine these lower and upper boundaries, be sure
to read about the automatic Canny edge detector in the
Chapter 10 supplementary material"""