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
"""
To compute our optimal value of T, we use the otsu function in the mahotas.
thresholding package. As our output
will later show us, Otsu’s method finds a value of T = 137
that we will use for thresholding"""

T = mahotas.thresholding.otsu(blurred)
print("Otsu’s threshold: {}".format(T))

"""Applying the thresholding is accomplished on Lines 19-
22. First, we make a copy of our grayscale image so that we
have an image to threshold. Line 32 then makes any values
greater than T white, whereas Line 34 makes all remaining
pixels that are not white into black pixels. We then invert
our threshold by using cv2.bitwise_not. This is equivalent
to applying a cv2.THRESH_BINARY_INV thresholding type as
in previous examples in this chapter"""

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

"""Another method to keep in mind when finding optimal
values for T is the Riddler-Calvard method. Just as in
Otsu’s method, the Riddler-Calvard method also computes
an optimal value of 137 for T. We apply this method on
Line 48 using the rc function in mahotas.thresholding. Finally, the actual thresholding of the image takes place on
Lines 51-54, as in the previous example. Given that the
values of T are identical for Otsu and Riddler-Calvard, the
thresholded image in Figure 9.3 (right) is identical to the
thresholded image in the center"""

T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)