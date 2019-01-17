import numpy as np 
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True , help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)

#average blurring

"""As the name suggests, we are going to define a k × k sliding window on top of our image, where k is always an odd
number. This window is going to slide from left-to-right
and from top-to-bottom. The pixel at the center of this matrix (we have to use an odd number, otherwise there would
not be a true “center”) is then set to be the average of all
other pixels surrounding it.
We call this sliding window a “convolution kernel” or
just a “kernel”. We’ll continue to use this terminology throughout this chapter.
As we will see, as the size of the kernel increases, the
more blurred our image will become"""

"""In order to average blur an image, we use the cv2.blur
function. This function requires two arguments: the image
we want to blur and the size of the kernel.we blur our image with increasing-sized kernels. The
larger our kernel becomes, the more blurred our image will
appear"""

"""We make use of the np.hstack function to stack our output images together. This method “horizontally stacks” our
three images into a row. This is useful since we don’t want
to create three separate windows using the cv2.imshow function."""

blurred_avg = np.hstack([cv2.blur(image, (3,3)), cv2.blur(image, (5,5)), cv2.blur(image, (7,7)) ])

#Gaussian blurring

"""The first argument
to the function is the image we want to blur. Then, similar to cv2.blur, we provide a tuple representing our kernel
size. Again, we start with a small kernel size of 3 × 3 and
start to increase it"""

blurred_Gauss = np.hstack([cv2.GaussianBlur(image, (3, 3), 0),cv2.GaussianBlur(image, (5, 5), 0),cv2.GaussianBlur(image, (7, 7), 0)])

"""The last parameter is our s, the standard deviation in the
x-axis direction. By setting this value to 0, we are instructing OpenCV to automatically compute them based on our
kernel size"""

#Mediam blurring

"""When applying a median blur, we first define our kernel
size k. Then, as in the averaging blurring method, we consider all pixels in the neighborhood of size k × k. But, unlike
the averaging method, instead of replacing the central pixel
with the average of the neighborhood, we instead replace
the central pixel with the median of the neighborhood"""

"""Median blurring is more effective at removing salt-andpepper style noise from an image because each central pixel
is always replaced with a pixel intensity that exists in the
image"""
"""Averaging and Gaussian methods can compute means or
weighted means for the neighborhood – this average pixel
intensity may or may not be present in the neighborhood.
But by definition, the median pixel must exist in our neighborhood. By replacing our central pixel with a median
rather than an average, we can substantially reduce noise."""

blurred_medi = np.hstack([cv2.medianBlur(image, 3), cv2.medianBlur(image, 5), cv2.medianBlur(image, 7)])

"""Applying a median blur is accomplished by making a call
to the cv2.medianBlur function. This method takes two parameters: the image we want to blur and the size of our
kernel. On Lines 25-27, we start off with a kernel size of 3, then increase it to 5 and 7.

Our median blurred images can be seen in Figure 8.4.
Notice that we are no longer creating a “motion blur” effect like in averaging and Gaussian blurring – instead, we
are removing detail and noise
"""

#Bilateral Blurring

"""In order to reduce noise while still maintaining edges, we
can use bilateral blurring. Bilateral blurring accomplishes this by introducing two Gaussian distributions

The first Gaussian function only considers spatial neighbors, that is, pixels that appear close together in the (x, y)
coordinate space of the image. The second Gaussian then models the pixel intensity of the neighborhood, ensuring
that only pixels with similar intensity are included in the actual computation of the blur.

Overall, this method is able to preserve edges of an image, while still reducing noise. The largest downside to this
method is that it is considerably slower than its averaging,
Gaussian, and median blurring counterparts
"""

blurred_bilateral = np.hstack([cv2.bilateralFilter(image, 5, 21, 21),cv2.bilateralFilter(image, 7, 31, 31),cv2.bilateralFilter(image, 9, 41, 41)])

""" The first parameter we supply
is the image we want to blur. Then, we need to define the
diameter of our pixel neighborhood. The third argument
is our color s. A larger value for color s means that more
colors in the neighborhood will be considered when computing the blur. Finally, we need to supply the space s. A
larger value of space s means that pixels farther out from
the central pixel will influence the blurring calculation, provided that their colors are similar enough"""

#showing the blurring image 
cv2.imshow("Averged",blurred_bilateral)
cv2.waitKey(0)