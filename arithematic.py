from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

"""According to our arithmetic rules, the subtraction should
return a value of −50; however, OpenCV once again performs clipping for us. We find that the value is clipped to a
value of 0. The second line of Listing 6.15 verifies this: subtracting 100 from 50 using cv2.subtract returns a value of
0"""

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
"""However, NumPy does not perform clipping – it instead
performs modulo arithmetic and “wraps around”. Once a
value of 255 is reached, NumPy wraps around to zero, and
then starts counting up again, until 100 steps have been
reached. You can see this is true via the first line of output
on Listing 6.16.
Then, we define two more NumPy arrays: one has a value
of 50 and the other 100. Using the cv2.subtract method,
this subtraction would be clipped to return a value of 0.
However, we know that NumPy performs modulo arithematic  rather than clipping. Instead, once 0 is reached during the subtraction, the modulos operations wraps around
and starts counting backwards from 255 – thus the result
on the second line of output"""

print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

"""defines a NumPy array of ones, with the same
size as our image. Again, we are sure to use 8-bit unsigned
integers as our data type. In order to fill our matrix with
values of 100’s rather than 1’s, we simply multiply our matrix of 1’s by 100. Finally, we use the cv2.add function to
add our matrix of 100’s to the original image – thus increasing every pixel intensity in the image by 100, but ensuring
all values are clipped to the range [0, 255] if they attempt to
exceed 255"""
M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)
