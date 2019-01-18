import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

"""At this point, we apply Gaussian blurring 
with a s = 5 radius. Applying Gaussian blurring helps remove some of the high frequency edges in the image that
we are not concerned with"""

"""we compute the thresholded image using the cv2.threshold function. This
method requires four arguments. The first is the grayscale
image that we wish to threshold. We supply our blurred
image here.

Then, we manually supply our T threshold value. We
use a value of T = 155.

Our third argument is our maximum value applied during thresholding. Any pixel intensity p that is greater than
T, is set to this value. In our example, any pixel value that
is greater than 155 is set to 255. Any value that is less than
155 is set to zero

Finally, we must provide a thresholding method. We use
the cv2.THRESH_BINARY method, which indicates that pixel
values p greater than T are set to the maximum value (the third argument)."""

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

"""The cv2.threshold function returns two values. The firstis T, 
the value we manually specified for thresholding. The second is our actual thresholded image
"""

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

cv2.imshow("Coins", cv2.bitwise_and(image, image, mask =threshInv))
cv2.waitKey(0)