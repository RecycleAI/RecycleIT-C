#importing libraries
import cv2
import math

#rescaling
def rescaleFrame(im, scale = 0.75):
    width = int(im.shape[1] * scale)
    height = int(im.shape[1] * scale)
    dimensions = (width, height)

    return cv2.resize(im, dimensions, interpolation=cv2.INTER_AREA)

#reading and resizing
im = cv2.imread('PET-6.jpg',cv2.IMREAD_GRAYSCALE)
resized_image = rescaleFrame(im)

_,im1 = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)
resized_image1 = rescaleFrame(im1)

cv2.imshow('Image', resized_image)
cv2.waitKey(0)

cv2.imshow('Image', resized_image1)
cv2.waitKey(0)

#raw moments
moments = cv2.moments(im)
print(moments)

#huMoments
huMoments = cv2.HuMoments(moments)
print(huMoments)

#converting huMoments
for i in range(0,7):
   huMoments[i] = -1* math.copysign(1.0, huMoments[i]) * math.log10(abs(huMoments[i]))
   print(huMoments[i])