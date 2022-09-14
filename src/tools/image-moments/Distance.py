#importing libraries
import cv2

#resclaing
def rescaleFrame(im1, scale = 0.75):
    # images, videos and live videos
    width = int(im1.shape[1] * scale)
    height = int(im1.shape[1] * scale)
    dimensions = (width, height)

    return cv2.resize(im1, dimensions, interpolation=cv2.INTER_AREA)

#reading and resizing
im1 = cv2.imread('PET.jpg',cv2.IMREAD_GRAYSCALE)
resized_image = rescaleFrame(im1)

im2 = cv2.imread('PET-6.jpg',cv2.IMREAD_GRAYSCALE)
resized_image = rescaleFrame(im2)

#calculating distances
d1 = cv2.matchShapes(im1,im2,cv2.CONTOURS_MATCH_I1,0)
print(d1)

d2 = cv2.matchShapes(im1,im2,cv2.CONTOURS_MATCH_I2,0)
print(d2)

d3 = cv2.matchShapes(im1,im2,cv2.CONTOURS_MATCH_I3,0)
print(d3)