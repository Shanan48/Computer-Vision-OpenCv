import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean Thresh", thresh)

thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Thresh", thresh)
cv2.waitKey(0)

"""We then apply adaptive thresholding to our blurred image using the cv2.adaptiveThreshold function .
The first parameter we supply is the image we want to
threshold. Then, we supply our maximum value of 255,
similar to simple thresholding mentioned above.

The third argument is our method to compute the threshold for the current neighborhood of pixels. By supplying
cv2.ADAPTIVE_THRESH_MEAN_C, we indicate that we want to
compute the mean of the neighborhood of pixels and treat it as our T value

Next, we need our thresholding method. Again, the description of this parameter is identical to the simple thresholding method mentioned above. 
We use cv2.THRESH_BINARY_INV to indicate that any pixel intensity greater than T in
the neighborhood should be set to 255, otherwise it should be set to 0.

The next parameter is our neighborhood size. This integer value must be odd and indicates how large our neighborhood of pixels is going to be.
 We supply a value of 11,
indicating that we are going to examine 11 × 11 pixel regions of the image, instead of trying to threshold the image
globally, as in simple thresholding methods.

Finally, we supply a parameter simply called C. This
value is an integer that is subtracted from the mean, allowing us to fine-tune our thresholding. We use C = 4 in this example

In general, choosing between mean adaptive thresholding and Gaussian adaptive thresholding requires a few experiments on your end. The most important parameters
to vary are the neighborhood size and C, the value you
subtract from the mean. By experimenting with this value,
you will be able to dramatically change the results of your
thresholding
"""

