import numpy as np 
import cv2 
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help="Path to the image")
args = vars(ap.parse_args())

image= cv2.imread(args['image'])
cv2.imshow('Original',image)

flipped = cv2.flip(image,1)
cv2.imshow("Flipped Horizontal",flipped)

flipped = cv2.flip(image,0)
cv2.imshow("Flipped Vertical",flipped)

flipped = cv2.flip(image,-1)
cv2.imshow("Flipped Horizontal and Vertical",flipped)
cv2.waitKey(0)
