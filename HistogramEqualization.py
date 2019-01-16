import numpy as np
from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

eq = cv2.equalizeHist(image)
"""Performing histogram equalization is done using just a
single function: cv2.equalizeHist, which accepts a single
parameter, the grayscale image we want to perform histogram equalization on. The last couple lines of code display our histogram equalized image"""

cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)