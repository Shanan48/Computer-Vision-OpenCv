import numpy as np 
import cv2 
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help="Path to the image")
args = vars(ap.parse_args())

image= cv2.imread(args['image'])
cv2.imshow('Original',image)
"""In this line of code, we define our new image width to be 150
pixels. In order to compute the ratio of the new height to
the old height, we simply define our ratio r to be the new
width (150 pixels) divided by the old width, which we access using image.shape[1]"""
#r = 150.0 / image.shape[1]
"""Now that we have our ratio, we can compute the new dimensions of the image.Again, the width of the
new image will be 150 pixels. The height is then computed
by multiplying the old height by our ratio and converting
it to an integer"""
#dim = (150, int(image.shape[0] * r))
"""The actual resizing of the image takes place on Line 17.
The first argument is the image we wish to resize and the
second is our computed dimensions for the new image.The
last parameter is our interpolation method, which is the
algorithm working behind the scenes to handle how the
actual image is resized. In general, I find that using cv2.
INTER_AREA obtains the best results when resizing; however, other appropriate choices include cv2.INTER_LINEAR,
cv2.INTER_CUBIC, and cv2.INTER_NEAREST."""
#resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
resized = imutils.resize(image, width = 100)
cv2.imshow("Resized (Width)", resized)

"""In the example we just explored, we only resized the image by specifying the width. But what if we wanted to
resize the image by specifying the height? All that requires
is a change to computing the aspect ratio:"""

#r = 50.0 / image.shape[0]
#dim = (int(image.shape[1] * r), 50)
#resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

resized = imutils.resize(image, height = 100)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)