import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
"""We then construct a NumPy array, filled with zeros, with
the same width and height as our beach image on Line 13.
In order to draw the white rectangle, we first compute the
center of the image on Line 17 by dividing the width and
height by two, using the // operator to indicate integer division. Finally, we draw our white rectangle on line 18"""

mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75), 255,-1)
cv2.imshow("Mask", mask)

"""We apply our mask on Line 18 using the cv2.bitwise_
and function. The first two parameters are the image itself. Obviously, 
the AND function will be True for all pixels in the image; however, the important part of this function 
is the mask keyword argument. By supplying a mask,
the cv2.bitwise_and function only examines pixels that are
“on” in the mask. In this case, only pixels that are part of
the white rectangle."""

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)