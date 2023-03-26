import cv2

# reading and resizing
im1 = cv2.imread('PET.jpg', cv2.IMREAD_GRAYSCALE)
resized_im1 = cv2.resize(im1, (0, 0), fx=0.75, fy=0.75, interpolation=cv2.INTER_AREA)

im2 = cv2.imread('PET-6.jpg', cv2.IMREAD_GRAYSCALE)
resized_im2 = cv2.resize(im2, (0, 0), fx=0.75, fy=0.75, interpolation=cv2.INTER_AREA)

# calculating distances
methods = [cv2.CONTOURS_MATCH_I1, cv2.CONTOURS_MATCH_I2, cv2.CONTOURS_MATCH_I3]
distances = [cv2.matchShapes(resized_im1, resized_im2, method, 0) for method in methods]
print(distances)
