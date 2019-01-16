from __future__ import print_function
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help="path to image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("original",image)

(b,g,r) = image[0,0]

print("The Red: {} , The Green: {} , The Blue: {} ".format(r,g,b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,
g, b))

#to make squre started from (0,0) pixel to (100,100)
corner = image[0:100 , 0:100]
cv2.imshow("Corner",corner)

#and make its colour greean
image[0:100 , 0:100] = (0,255,0)
cv2.imshow("updated",image)
cv2.waitKey(0)