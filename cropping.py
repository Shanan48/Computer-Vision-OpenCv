import numpy as np 
import cv2 
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help="Path to the image")
args = vars(ap.parse_args())

image= cv2.imread(args['image'])
cv2.imshow('Original',image)
"""We are supplying NumPy array slices to extract
a rectangular region of the image, starting at (240, 30) and
ending at (335, 120). The order in which we supply the
indexes to the crop may seem counterintuitive; however, remember that OpenCV represents images as NumPy arrays
with the the height first and the width second. This means
that we need to supply our y-axis values before our x-axis."""
cropped = image[30:120 , 240:335]
cv2.imshow("T-Rex Face", cropped)
cv2.waitKey(0)

"""In order to perform our cropping, NumPy expects four
indexes:
1. Start y: The starting y coordinate. In this case, we
start at y = 30.
2. End y: The ending y coordinate. We will end our crop
at y = 120.
3. Start x: The starting x coordinate of the slice. We start
the crop at x = 240 
4. End x: The ending x-axis coordinate of the slice. Our
slice ends at x = 335."""