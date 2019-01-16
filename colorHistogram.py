from __future__ import print_function
from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("’Flattened’ Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	plt.plot(hist, color = color)
	plt.xlim([0, 256])
	plt.show()

"""I like to explain multi-dimensional histograms by using
the word AND.
For example, we can ask a question such as, “How many
pixels have a Red value of 10 AND a Blue value of 30?”.
How many pixels have a Green value of 200 AND a Red
value of 130? By using the conjunctive AND, we are able to
construct multi-dimensional histograms.
It’s that simple. Let’s check out some code to automate
the process of building a 2D histogram:
"""
fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None,[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None,[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None,[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

"""Using a 2D histogram takes into account two channels at
a time. But what if we wanted to account for all three RGB
channels? You guessed it. We’re now going to build a 3D
histogram."""

hist = cv2.calcHist([image], [0, 1, 2],None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))
plt.show()

"""The code here is very simple – it’s just an extension of the
code above. We are now computing an 8 × 8 × 8 histogram
for each of the RGB channels. We can’t visualize this histogram, but we can see that the shape is indeed (8,8,8)
with 512 values."""