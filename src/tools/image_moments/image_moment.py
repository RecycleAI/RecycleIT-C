import cv2
import math

def rescale_frame(image, scale=0.75):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)

# Load the image and resize it
image = cv2.imread('PET-6.jpg', cv2.IMREAD_GRAYSCALE)
resized_image = rescale_frame(image)

# Apply thresholding to the image and resize it
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
resized_binary_image = rescale_frame(binary_image)

# Display the images
cv2.imshow('Original Image', resized_image)
cv2.imshow('Thresholded Image', resized_binary_image)
cv2.waitKey(0)

# Compute the raw moments and Hu moments
moments = cv2.moments(image)
hu_moments = cv2.HuMoments(moments)

# Define a function to convert Hu moments to a more readable format
def convert_hu_moments(moments):
    converted_moments = []
    for i in range(0, 7):
        moment = -1 * math.copysign(1.0, moments[i]) * math.log10(abs(moments[i]))
        converted_moments.append(moment)
    return converted_moments

# Convert the Hu moments and print them
converted_hu_moments = convert_hu_moments(hu_moments)
print(converted_hu_moments)
