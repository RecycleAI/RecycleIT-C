import os
import numpy as np
import cv2

# map colour names to HSV ranges
color_list = [
    ['red', [136, 87, 111], [180, 250, 250]],
    ['yellow', [22, 60, 200], [60, 250, 250]],
    ['green', [40, 100, 100], [80, 250, 250]],
    ['blue', [78, 158, 124], [138, 250, 250]],
]


def detect_main_color(hsv_image, colors):
    color_found = 'undefined'
    max_count = 0

    for color_name, lower_val, upper_val in colors:
        # threshold the HSV image - any matching color will show up as white
        mask = cv2.inRange(hsv_image, np.array(lower_val), np.array(upper_val))

        # count white pixels on mask
        count = np.sum(mask)
        if count > max_count:
            color_found = color_name
            max_count = count

    return color_found


for root, dirs, files in os.walk('./images'):
    f = os.path.basename(root)

    for file in files:
        img = cv2.imread(os.path.join(root, file))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        print(f"{file}: {detect_main_color(hsv, color_list)}")