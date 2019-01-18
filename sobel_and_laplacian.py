"""The first thing we are going to do is find the “gradient” of
the grayscale image, allowing us to find edge-like regions in the x and y direction.

We’ll then apply Canny edge detection, a multi-stage process of noise reduction (blurring), finding the gradient of
the image (utilizing the Sobel kernel in both the horizontal and vertical direction), non-maximum suppression, and
hysteresis thresholding."""

from __future__ import print_function
import numpy as np
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

"""On Line 29, we use the Laplacian method to compute the
gradient magnitude image by calling the cv2.Laplacian
function. The first argument is our grayscale image – the
image we want to compute the gradient magnitude representation for. The second argument is our data type for the
output image."""

lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

""""Throughout this book, we have mainly used 8-bit unsigned integers. Why are we using a 64-bit float now?
The reason involves the transition of black-to-white and
white-to-black in the image.
Transitioning from black-to-white is considered a positive slope, whereas a transition from white-to-black is a
negative slope. If you remember our discussion of image
arithmetic in Chapter 6, you’ll know that an 8-bit unsigned
integer does not represent negative values Either it will be
clipped to zero if you are using OpenCV or a modulus operation  will be performed using NumPy.

The short answer here is that if you don’t use a floating
point data type when computing the gradient magnitude
image, you will miss edges, specifically the white-to-black transitions
 
In order to ensure you catch all edges, use a floating point
data type, then take the absolute value of the gradient image and convert it back to an 8-bit unsigned integer, as in
Line 15. This is definitely an important technique to take
note of – otherwise you’ll be missing edges in your image!"""

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

"""In fact, that’s exactly what Lines 52 and 53 do by using the cv2.Sobel method. The first argument to the Sobel
operator is the image we want to compute the gradient representation for. Then, just like in the Laplacian example
above, we use a floating point data type. The last two arguments are the order of the derivatives in the x and y direction, respectively. Specify a value of 1 and 0 to find vertical
edge-like regions and 0 and 1 to find horizontal edge-like regions"""

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

"""On Lines 60 and 61 we then ensure we find all edges by
taking the absolute value of the floating point image and
then converting it to an 8-bit unsigned integer"""

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

"""In order to combine the gradient images in both the x
and y direction, we can apply a bitwise OR. Remember, an
OR operation is true when either pixel is greater than zero.
Therefore, a given pixel will be True if either a horizontal
or vertical edge is present"""

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)