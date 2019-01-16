import numpy as np 
import cv2 
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help="Path to the image")
args = vars(ap.parse_args())

image= cv2.imread(args['image'])
cv2.imshow('Original',image)

#(h,w) = image.shape[:2]
#center = (w // 2,h // 2)

"""The cv2.getRotationMatrix2D function takes three arguments: the point at which we want to rotate the image
around (in this case, the center of the image). We then
specify q, the number of degrees we are going to rotate the
image by. In this case, we are going to rotate the image 45
degrees. The last argument is the scale of the image. We
haven’t discussed resizing an image yet, but here you can
specify a floating point value, where 1.0 means the same dimensions of the image are used. However, if you specified
a value of 2.0 the image would be doubled in size. Similarly,
a value of 0.5 halves the size of the image."""

#M = cv2.getRotationMatrix2D(center,45,.5)

#M = cv2.getRotationMatrix2D(center,45,1.0)
"""Once we have our rotation matrix M from the cv2.getRot
ationMatrix2D function, we can apply the rotation to our
image using the cv2.warpAffine method on Line 18. The
first argument to this function is the image we want to rotate. We then specify our rotation matrix M along with the
output dimensions (width and height) of our image. Line
19 then shows our image rotated by 45 degrees. Check out
Figure 6.2 Top-Right to see our rotated image."""

rotated = imutils.rotate(image,180)
cv2.imshow("rotated By 45 degree",rotated)
cv2.waitKey()

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)