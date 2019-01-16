import numpy as np 
import cv2 
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help="Path to the image")
args = vars(ap.parse_args())

image= cv2.imread(args['image'])
cv2.imshow('Original',image)
#define our translation matrix M
#M = np.float32([ [1,0,25] , [0,1,50] ])
""" This matrix tells us how
many pixels to the left or right, and up or down, the image
will be shifted ,The first row of the matrix
is [1, 0, tx], where tx is the number of pixels we will shift
the image left or right. Negative values of tx will shift the
image to the left and positive values will shift the image to
the right."""
#shifted = cv2.warpAffine(image, M ,(image.shape[1],image.shape[0]))

#use the package imutils that have function to do translation

shifted = imutils.translate(image,0,100)

cv2.imshow("Shifted Right and Down",shifted)

M = np.float32([ [1,0,-50], [0,1,-90] ])
shifted = cv2.warpAffine(image, M , (image.shape[1],image.shape[0]))

cv2.imshow("Left Up and Up",shifted)
cv2.waitKey()
