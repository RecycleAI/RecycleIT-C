import cv2
import matplotlib.pyplot as plt
import numpy as np

# Define a function to compute Hu moments
def compute_hu_moments(image):
    # Compute the raw moments and Hu moments
    moments = cv2.moments(image)
    hu_moments = cv2.HuMoments(moments)

    # Convert the Hu moments to a more readable format
    converted_moments = []
    for i in range(0, 7):
        moment = -1 * np.copysign(1.0, hu_moments[i]) * np.log10(abs(hu_moments[i]))
        converted_moments.append(moment)

    return converted_moments

# Define a function to plot a scatter chart for Hu moments
def plot_scatter_chart(hu_moments, ax):
    ax.scatter(range(1, 8), hu_moments)
    ax.set_xticks(range(1, 8))
    ax.set_xticklabels(['Hu1', 'Hu2', 'Hu3', 'Hu4', 'Hu5', 'Hu6', 'Hu7'])
    ax.set_xlabel('Hu moments')
    ax.set_ylabel('Value')
    ax.set_title('Scatter chart of Hu moments')

# Define a function to plot a bar chart for the grayscale image
def plot_bar_chart(image, ax):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    ax.bar(range(256), histogram.flatten(), width=1)
    ax.set_xlabel('Pixel value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of grayscale image')

# Define a function to plot a heatmap for the grayscale image
def plot_heatmap(image, ax):
    ax.imshow(image, cmap='gray')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Heatmap of grayscale image')

# Load multiple images and compute Hu moments for each image
images = ['PET.jpg', 'PET-2.jpg', 'PET-3.jpg', 'PET-4.jpg', 'PET-5.jpg', 'PET-6.jpg', 'PE-HD-2.jpg']
hu_moments_list = []
for image_path in images:
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    hu_moments = compute_hu_moments(image)
    hu_moments_list.append(hu_moments)

# Create subplots for each image and chart type
fig, axs = plt.subplots(len(images), 3, figsize=(15, len(images)*5))

for i, hu_moments in enumerate(hu_moments_list):
    image_path = images[i]
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    plot_scatter_chart(hu_moments, axs[i][0])
    plot_bar_chart(image, axs[i][1])
    plot_heatmap(image, axs[i][2])

plt.tight_layout()
plt.show()
