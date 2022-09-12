import cv2
import math

im = cv2.imread('PET-6.jpg',cv2.IMREAD_GRAYSCALE)

def rescaleFrame(im, scale = 0.75):
    # images, videos and live videos
    width = int(im.shape[1] * scale)
    height = int(im.shape[1] * scale)
    dimensions = (width, height)

    return cv2.resize(im, dimensions, interpolation=cv2.INTER_AREA)

resized_image = rescaleFrame(im)
cv2.imshow('Image', resized_image)
cv2.waitKey(0)


_,im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)
def rescaleFrame(im, scale = 0.75):
    # images, videos and live videos
    width = int(im.shape[1] * scale)
    height = int(im.shape[1] * scale)
    dimensions = (width, height)

    return cv2.resize(im, dimensions, interpolation=cv2.INTER_AREA)

resized_image = rescaleFrame(im)
cv2.imshow('Image', resized_image)
cv2.waitKey(0)

moments = cv2.moments(im)
print(moments)

huMoments = cv2.HuMoments(moments)
print(huMoments)

for i in range(0,7):
   huMoments[i] = -1* math.copysign(1.0, huMoments[i]) * math.log10(abs(huMoments[i]))
   print(huMoments[i])