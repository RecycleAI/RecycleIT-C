import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

def rescale_frame(image, scale=0.75):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)

# Define a function to convert Hu moments to a more readable format
def convert_hu_moments(moments):
    converted_moments = []
    for i in range(0, 7):
        moment = -1 * math.copysign(1.0, moments[i]) * math.log10(abs(moments[i]))
        converted_moments.append(moment)
    return converted_moments

# Load the images
images = ['PET.jpg', 'PET-2.jpg', 'PET-3.jpg', 'PET-4.jpg', 'PET-5.jpg', 'PET-6.jpg', 'PE-HD-2.jpg']

# Create a grid of subplots
fig, axs = plt.subplots(nrows=len(images), ncols=5, figsize=(20, 4*len(images)))

# Iterate over each image and plot the charts
for i, image_path in enumerate(images):
    # Load the image and resize it
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    resized_image = rescale_frame(image)

    # Apply thresholding to the image and resize it
    _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    resized_binary_image = rescale_frame(binary_image)

    # Compute the raw moments and Hu moments
    moments = cv2.moments(image)
    hu_moments = cv2.HuMoments(moments)
    converted_hu_moments = convert_hu_moments(hu_moments)

    # Plot the bar chart
    axs[i, 1].bar(range(len(converted_hu_moments)), converted_hu_moments)
    axs[i, 1].set_title('Image {} - Bar Chart'.format(i+1))
    
    # Plot the scatter chart
    axs[i, 0].scatter(converted_hu_moments, [0]*len(converted_hu_moments))
    axs[i, 0].set_title('Image {} - Scatter Chart'.format(i+1))

    # Plot the grayscale heatmap
    gray_heatmap = cv2.applyColorMap(resized_image, cv2.COLORMAP_BONE)
    axs[i, 3].imshow(gray_heatmap)
    axs[i, 3].set_title('Image {} - Grayscale Heatmap'.format(i+1))

    # Plot the colored histogram
    axs[i, 4].hist(image.ravel(), bins=256, range=[0, 256], color='r')
    axs[i, 4].set_title('Image {} - Colored Histogram'.format(i+1))

    # Plot the color heatmap
    color_heatmap = cv2.applyColorMap(resized_image, cv2.COLORMAP_HOT)
    axs[i, 2].imshow(color_heatmap)
    axs[i, 2].set_title('Image {} - Color Heatmap'.format(i+1))

# Add a title and save the chart
fig.suptitle('Comparison of Image Analysis Charts')
plt.savefig('comparison of Image Analysis Charts')